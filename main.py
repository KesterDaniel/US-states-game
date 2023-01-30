import turtle
import pandas
from turtle import Screen

timmy = turtle.Turtle()
timmy.hideturtle()

screen = Screen()
screen.setup(725, 491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
user_answers = []

while game_is_on:
    answer = screen.textinput(title=f"{len(user_answers)}/50 states correct", prompt="What's another state's name?").title()
    states = pandas.read_csv("50_states.csv")
    correct_state = states[states.state == answer]
    if not correct_state.empty and answer not in user_answers:
        xcord = int(correct_state.x)
        ycord = int(correct_state.y)
        timmy.penup()
        timmy.goto(xcord, ycord)
        timmy.write(answer.title(), align="center", font=('Arial', 8, 'normal'))
        user_answers.append(answer)

    if len(user_answers) == 50:
        game_is_on = False


screen.exitonclick()