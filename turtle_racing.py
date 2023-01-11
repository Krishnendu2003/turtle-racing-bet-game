from turtle import Turtle,Screen
import random

is_race_on=False
colors=["red","orange","yellow","green","blue","purple"]
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race?"
                                                       "options:red,orange,yellow,green,blue,purple ")
y_positions=[-70,-40,-10,20,50,80]
all_turtle=[]

if user_bet:
    is_race_on=True


for turtle_index in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230,y=y_positions[turtle_index] )
    all_turtle.append(new_turtle)


while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've win.The {winning_color} turtle wins the race")

            else:
                print(f"You loose.The {winning_color} turtle wins the race")



        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
input()