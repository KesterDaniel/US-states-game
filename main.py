import turtle
import pandas
from turtle import Screen

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

User_Score = 0
game_is_on = True

while game_is_on:
    answer = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()
    states = pandas.read_csv("50_states.csv")
    correct_state = states[states.state == answer]
    print(correct_state)
    game_is_on = False


screen.exitonclick()