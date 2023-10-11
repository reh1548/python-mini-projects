import turtle
import csv

# Step 1: Read data from CSV and prepare the data - State names and their coordinates
states_data = {}
with open("Day_25/US_State_Game/50_states.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        state_name = row["state"]
        x = int(row["x"])
        y = int(row["y"])
        states_data[state_name] = (x, y)

# Step 2: Show the input box
def get_user_input():
    return turtle.textinput("Guess the State", "Enter a state name:")


def main():
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "Day_25/US_State_Game/blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    # Step 3: Create a turtle for the scoreboard
    scoreboard = turtle.Turtle()
    scoreboard.hideturtle()
    scoreboard.penup()
    scoreboard.goto(0, 260)
    scoreboard.write("Correct Guesses: 0/50", align="center", font=("Arial", 16, "normal"))


    # Step 4: Check the answers
    correct_guesses = 0
    while correct_guesses < 50:  # Loop until all states are guessed correctly
        user_input = get_user_input()
        if user_input is None:
            break  # If the user cancels the input box, exit the loop
        user_guess = user_input.title()

        if user_guess in states_data:
            # Step 5: Display correct answers
            correct_guesses += 1
            x, y = states_data[user_guess]
            marker = turtle.Turtle()
            marker.penup()
            marker.hideturtle()
            marker.goto(x, y)
            marker.write(user_guess, align="center", font=("Arial", 8, "normal"))

            
        # Step 6: Update the scoreboard
        scoreboard.clear()
        scoreboard.write(f"Correct Guesses: {correct_guesses}/50", align="center", font=("Arial", 16, "normal"))


    turtle.done()
    accuracy = (correct_guesses / 50) * 100
    print(f"You guessed {correct_guesses} out of 50 states correctly. Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    main()
