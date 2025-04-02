import colorgram
import turtle as t
from random import choice, randint

color_list = []
colors = colorgram.extract('dh_spots.jpg', 20)
t.colormode(255)

hirst = t.Turtle()
hirst.speed('fastest')
hirst.penup()
hirst.hideturtle()


# Extract colors from the image
for each_color in colors:
    color_list.append((each_color.rgb.r, each_color.rgb.g, each_color.rgb.b))


def draw_hirst_painting(dots, dots_size, dots_space, rows):
    row_start_x = ((dots - 1) * dots_space) / 2
    row_start_y = ((rows - 1) * dots_space) / 2
    
    for i in range(rows):
        hirst.goto(-row_start_x, -row_start_y)
        for _ in range(dots):
            hirst.setheading(0)
            hirst.dot(dots_size, choice(color_list))
            hirst.forward(dots_space)
        row_start_y -= dots_space
        print(f"{i} row done - y: {row_start_y}")


draw_hirst_painting(10,20, 50, 5 )
t.exitonclick()

