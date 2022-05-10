import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import turtle
from random import randint

def draw_grid():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-300, 300)
    turtle.pendown()
    turtle.goto(300, 300)
    turtle.goto(300, -300)
    turtle.goto(-300, -300)
    turtle.goto(-300, 300)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.goto(0, 300)
    turtle.goto(300, 300)
    turtle.goto(300, 0)
    turtle.goto(0, 0)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.goto(0, -300)
    turtle.goto(-300, -300)
    turtle.goto(-300, 0)
    turtle.goto(0, 0
