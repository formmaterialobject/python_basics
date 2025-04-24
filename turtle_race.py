from turtle import Turtle, Screen
from random import randint 

race_screen = Screen()
race_screen.setup(width=800, height=400)

#finishline
finish_line = Turtle()
finish_line.hideturtle()
finish_line.penup()
finish_line.goto(x = 380, y = -200)
finish_line.setheading(90)
finish_line.pendown()
finish_line.forward(400)    

#create some turtles
def create_turtle():
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]
    turtles = []
    for i in range(len(colors)):
        turtle = Turtle(shape="turtle")
        turtle.color(colors[i])
        turtle.penup()
        turtle.goto(x = -380, y = (-125 + (50*i)))
        turtles.append(turtle)
    return turtles

def turtle_moving(turtles):
    for turtle in turtles:
        random_distance = randint(2, 10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 380:
            winning_color = turtle.pencolor()
            return True, winning_color
    return False, None


turtles = create_turtle()

user_bet = race_screen.textinput("Make your bet", "Which turtle will win? Enter a color: ").lower()
print(user_bet)

while True:
    is_race_over, winning_color = turtle_moving(turtles)
    if is_race_over:
        print(f"The {winning_color} turtle is the winner!")
        break

if winning_color == user_bet:
    print("You win!")
else:
    print("You lose!")

print("Game Over")

race_screen.exitonclick()