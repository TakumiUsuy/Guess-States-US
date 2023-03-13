import turtle
import pandas as p

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = 0
data = p.read_csv("50_states.csv")
states = data["state"].to_list()
x_list = data["x"].to_list()
y_list = data["y"].to_list()

while score != 50:
    answer = screen.textinput(title=f"{score}/50", prompt="What's another state's name?").title()
    if answer in states:
        t = turtle.Turtle()
        x = x_list[states.index(answer)]
        y = y_list[states.index(answer)]
        states.remove(answer)
        t.hideturtle()
        t.penup()
        t.goto(int(x), int(y))
        t.write(answer)
        score += 1
    if answer == 'Exit':
        missing_states = {
            "States": []
        }
        missing_states["States"].append(states)
        p.DataFrame(missing_states).to_csv("Missing states")
        break
