import sys
from tkinter import *
from tkinter import messagebox
import string
import secrets
import json

# Redirect standard error to a custom stream
class StdErrRedirector:
    def write(self, message):
        # Show warning pop-up
        messagebox.showwarning("Warning", message.strip())

# Set the custom stream as stderr
sys.stderr = StdErrRedirector()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Choose a random password length between 12 and 16 characters
    password_length = secrets.randbelow(5) + 12

    # Generate the password by randomly selecting characters from the defined set
    password = ''.join(secrets.choice(characters) for i in range(password_length))

    # Update the Password Entry field with the generated password
    entry3.delete(0, END)
    entry3.insert(END, password)

# ---------------------------- SAVE CREDENTIALS ------------------------------- #
def save_credentials():
    website = entry1.get()
    username = entry2.get()
    password = entry3.get()

    # Check if any field is empty
    if not website or not username or not password:
        messagebox.showwarning("Missing Fields", "Please fill up all the fields before saving.")
    else:
        credentials = {
            "username": username,
            "password": password
        }

        try:
            with open("Day_29/Password Manager/credentials.json", "r") as file:
                data = json.load(file)
                
            # Find the index of the website entry if it already exists
            website_index = next((index for index, entry in enumerate(data["websites"]) if entry["name"] == website), None)

            if website_index is not None:
                data["websites"][website_index]["credentials"].append(credentials)
            else:
                data["websites"].append({
                    "name": website,
                    "credentials": [credentials]
                })

        except (FileNotFoundError, json.JSONDecodeError):
            data = {"websites": [{"name": website, "credentials": [credentials]}]}

        with open("Day_29/Password Manager/credentials.json", "w") as file:
            json.dump(data, file, indent=4)
        
        # Clear the entry fields after saving
        entry1.delete(0, "end")
        entry2.delete(0, "end")
        entry3.delete(0, "end")

# ---------------------------- SEARCH CREDENTIALS BY WEBSITE------------------------------- #
def search_by_website():
    website = entry1.get()
    with open("Day_29/Password Manager/credentials.json", "r") as file:
        credentials_database = json.load(file)
    
    found_credentials = []

    if not website:  # If website field is empty, show all data
        for website_data in credentials_database["websites"]:
            website_name = website_data["name"]
            for credential in website_data["credentials"]:
                username = credential["username"]
                password = credential["password"]
                found_credentials.append(f"Website: {website_name}\nUsername: {username}\nPassword: {password}\n")
    else:
        for website_data in credentials_database["websites"]:
            if website_data["name"] == website:
                website_name = website_data["name"]
                for credential in website_data["credentials"]:
                    username = credential["username"]
                    password = credential["password"]
                    found_credentials.append(f"Website: {website_name}\nUsername: {username}\nPassword: {password}\n")

    if not found_credentials:
        messagebox.showinfo("Search Result", f"No credentials found for {website}.")
    else:
        credentials_text = "\n".join(found_credentials)

        # Create a new window to display the search result
        result_window = Toplevel(window)
        result_window.title("Search Result")

        # Create a Text widget to display the credentials
        text_widget = Text(result_window, wrap=WORD, width=50, height=15)
        text_widget.insert(END, credentials_text)
        text_widget.pack(fill=BOTH, expand=True)

        # Allow the text to be selected and copied
        text_widget.configure(state="disabled")



# ---------------------------- UPDATE OR DELETE CREDENTIALS------------------------------- #
def modify():
    with open("Day_29/Password Manager/credentials.json", "r") as file:
        credentials_database = json.load(file)

    credentials_list = []

    for website_data in credentials_database["websites"]:
            website_name = website_data["name"]
            for credential in website_data["credentials"]:
                username = credential["username"]
                password = credential["password"]
                credentials_list.append(f"Website: {website_name}\nUsername: {username}\nPassword: {password}\n")
    
    credentials_text = "\n".join(credentials_list)

    modify_window = Toplevel(window)
    modify_window.title("Modify")

    # Create a Text widget to display the credentials
    text_widget = Text(modify_window, wrap=WORD, width=50, height=15)
    text_widget.insert(END, credentials_text)
    text_widget.pack(fill=BOTH, expand=True)

    # Allow the text to be edited
    text_widget.configure(state="normal")

    def save_and_close():
        # Implement your save logic here
        # Extract and update the modified credentials
        # Save the updated data back to the file
        # Close the window
        modify_window.destroy()

    def on_closing():
        if messagebox.askokcancel("Confirm", "Are you sure you want to modify?"):
            save_and_close()

    # Add buttons for Save and Ok
    save_button = Button(modify_window, text="Save", command=on_closing)
    save_button.pack()

    modify_window.protocol("WM_DELETE_WINDOW", on_closing)




# # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
img = PhotoImage(file="Day_29/Password Manager/logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

label = Label(text="Website: ")
label.grid(column=0, row=1)

#Entry for Website
entry1 = Entry(width=50)
entry1.insert(END, string="")
entry1.grid(column=1, row=1)


label = Label(text="Email/Username: ")
label.grid(column=0, row=2)

#Entry for Email/Username
entry2 = Entry(width=50)
entry2.insert(END, string="")
entry2.grid(column=1, row=2)

label = Label(text="Password: ")
label.grid(column=0, row=3)

#Entry for Password
entry3 = Entry(width=50)
entry3.insert(END, string="")
entry3.grid(column=1, row=3)

# #Credentials Search by Website Button
button1 = Button(width=15, text="Search", command=search_by_website)
button1.grid(column=2, row=1)

#Password Generator Button
button2 = Button(width=15, text="Generate Password", command=password_generator)
button2.grid(column=2, row=3)

#Add newly created credentials
button3 = Button(width=42, text="Add", command=save_credentials)
button3.grid(column=1, row=4)

#Add newly created credentials
button4 = Button(width=42, text="Modify", command=modify)
button4.grid(column=1, row=5)

window.mainloop()
