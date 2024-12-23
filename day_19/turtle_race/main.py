import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            # Declare the winner and stop further checks
            pen = Turtle()
            pen.color(winning_color)
            pen.hideturtle()
            pen.penup()
            pen.goto(0, 150)

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner!")
                pen.write(f"You've won! The {winning_color} is the winner!", align="center", font=("Arial", 24, "normal"))
            else:
                print(f"You've lost! The {winning_color} is the winner!")
                pen.write(f"You've lost! The {winning_color} is the winner!", align="center", font=("Arial", 24, "normal"))
            # Exit the loop immediately
            break

        # Move the turtle randomly
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
