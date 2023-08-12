from turtle import Turtle

FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        
    def write_answer(self, state_name, x_coor, y_coor):
        new_answer = Turtle()
        new_answer.hideturtle()
        new_answer.penup()
        new_answer.goto(x_coor, y_coor)
        new_answer.write(
            f"{state_name}",
            align = "center",
            font = FONT
            )
        
        