from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['UPLOAD_FOLDER'] = 'C:/Users/re323/projects/100_days_python/100_days_python_bootcamp-1/Day_68/static/files'
# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

# Configure Flask-Login's Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

 
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")



@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        #Creating hased password
        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )

        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            #Saving hashed password in DB
            password=hash_and_salted_password,
        )

        db.session.add(new_user)
        db.session.commit()

        # Log in and authenticate user after adding details to database.
        login_user(new_user)

        # Can redirect() and get name from the current_user
        return redirect(url_for("secrets"))

    return render_template("register.html")


# @app.route('/login', methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         email = request.form.get('email')
#         password = request.form.get('password')

#         # Find user by email entered.
#         result = db.session.execute(db.select(User).where(User.email == email))
#         user = result.scalar() if result else None
#         if user is not None:
#             user = result.scalar()
#             # Check stored password hash against entered password hashed.
#             if check_password_hash(user.password, password):
#                 login_user(user)
#                 return redirect(url_for('secrets'))
#             else:
#                 flash('Wrong Password.')
#         else:
#             flash('This email does not exist.')


#     return render_template("login.html")
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        # Find user by email entered.
        user = User.query.filter_by(email=email).first()  # Simplified query

        if user:
            # Check stored password hash against entered password hashed.
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('secrets'))
            else:
                flash('Wrong Password.')
        else:
            flash('This email does not exist.')

    return render_template("login.html")


# Only logged-in users can access the route
@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    logout_user()
    
    return redirect(url_for('home'))


@app.route('/download/<path:name>', methods=['GET'])
def download(name):
    return send_from_directory(
        app.config['UPLOAD_FOLDER'], name, as_attachment=True
    )



if __name__ == "__main__":
    app.run(debug=True)
