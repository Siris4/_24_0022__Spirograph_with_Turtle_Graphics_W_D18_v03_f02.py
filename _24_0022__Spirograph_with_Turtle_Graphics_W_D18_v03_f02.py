import turtle as t  #we have to change the actual turtle Module, not the object
import random
from turtle import Screen

tiptup = t.Turtle()

#TODO 1: Thickness of the paint
tiptup.pensize(width=1)
tiptup.width(width=1)

#TODO 2: Speed that it "walks"
tiptup.speed('fastest')

# Color:
t.colormode(255)

# movement_list = [90, 180, 270, 360]

def random_color_generator():
    # global r, g, b, rgb
    # (r, g, b) = ""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = (r, g, b)
    return rgb_color

# print(rgb)


# circle_angle = ""

def draw_a_circle():
    tiptup.circle(100)
    tiptup.right(angle=-2)




for _ in range(350):
    global circle_angle
    circle_angle = 5
    tiptup.color(random_color_generator())
    #rgb(168, 145, 0)
    draw_a_circle()
    circle_angle += -5

screen = Screen()
screen.exitonclick()