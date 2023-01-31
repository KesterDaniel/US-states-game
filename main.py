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

states = pandas.read_csv("50_states.csv")

while game_is_on:
    answer = screen.textinput(title=f"{len(user_answers)}/50 states correct", prompt="What's another state's name?") \
        .title()

    if answer == "Exit":
        break
    correct_state = states[states.state == answer]
    if not correct_state.empty and answer not in user_answers:
        xcord = int(correct_state.x)
        ycord = int(correct_state.y)
        timmy.penup()
        timmy.goto(xcord, ycord)
        timmy.write(answer.title(), font=('Arial', 8, 'normal'))
        user_answers.append(answer)

    if len(user_answers) == 50:
        game_is_on = False

states_list = states["state"].to_list()
missing_states = []
missing_states_x = []
missing_states_y = []

for state in states_list:
    if state not in user_answers:
        missing_state = states[states["state"] == state]
        missing_state_xcoord = missing_state.x
        missing_state_xvalue = missing_state_xcoord.item()
        missing_state_ycoord = missing_state.y
        missing_state_yvalue = missing_state_ycoord.item()
        missing_states.append(state)
        missing_states_x.append(missing_state_xvalue)
        missing_states_y.append(missing_state_yvalue)

states_to_learn = {
    "state": missing_states,
    "x": missing_states_x,
    "y": missing_states_y
}

states_to_learn_data = pandas.DataFrame(states_to_learn)
states_to_learn_data.to_csv("states_to_learn.csv")
