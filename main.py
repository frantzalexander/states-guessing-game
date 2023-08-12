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

states_remaining = df["state"].to_list()


def ask_question():
    answer_question = turtle.textinput(
        title = f"{len(guessed_states)}/50 States Correct",
        prompt = "What's another state's name?"
    )
    
    capitalized_answer = answer_question.title()
    
    return capitalized_answer

scoreboard = Scoreboard()

guessed_states = [] 
score = 0

while len(guessed_states) < 50:
    
    answer_state = ask_question()
    
    if answer_state == "Exit":
        for state in guessed_states:
            states_remaining.remove(state)
        
        states_to_learn = pd.DataFrame(data = states_remaining)
        states_to_learn.to_csv("states_to_learn.csv", index = False)
        break
        

    if answer_state in all_states:
        score += 1
        guessed_states.append(answer_state)
        state_data = df[df["state"] == answer_state]
        x_location = int(state_data.iloc[0]["x"])
        y_location = int(state_data.iloc[0]["y"])
        
        scoreboard.write_answer(
            state_name = answer_state,
            x_coor = x_location,
            y_coor = y_location
            )

turtle.mainloop()
