import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Tetris")

# Set up the screen
wn = turtle.Screen()
wn.title("Tetris")
wn.bgcolor("black")
wn.setup(width=600, height=800)
wn.tracer(0)

# Score
score = 0

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -400)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Create the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 360)
scorestring = "Score: %s" %score
score_pen
