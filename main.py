import turtle
from turtle import Screen

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer = screen.textinput(title="Guess the state", prompt="What's another state's name?")
print(answer)


screen.exitonclick()