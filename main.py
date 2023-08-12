import turtle
import pandas as pd

from scoreboard import Scoreboard

csv_file = "50_states.csv"

image = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S States Game")
screen.addshape(image)

turtle.shape(image)

df = pd.read_csv(csv_file)

all_states = df["state"].to_list()

def ask_question():
    answer_question = turtle.textinput(
        title = f"Score: {score} Guess the State",
        prompt = "What's another state's name?"
    )
    
    capitalized_answer = answer_question.title()
    
    return capitalized_answer

scoreboard = Scoreboard()

guesses_listing = [] 
score = 0

game_is_on = True
while game_is_on:
    
    answer_state = ask_question()

    if answer_state in all_states:
        score += 1
        guesses_listing.append(answer_state)
        state_data = df[df["state"] == answer_state]
        x_location = int(state_data.iloc[0]["x"])
        y_location = int(state_data.iloc[0]["y"])
        
        scoreboard.write_answer(
            state_name = answer_state,
            x_coor = x_location,
            y_coor = y_location
            )
        

turtle.mainloop()