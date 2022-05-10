import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# 가로 세로 값을 입력하면 사각형을 그리는 프로그램을 만드세요.

import turtle

turtle.shape('turtle')

width = int(input('가로 세로 값을 입력하세요 : '))

for i in range(4):
    turtle.forward(width)
    turtle.left(90)

turtle.exitonclick()

# 홀수를 입력하면 그 홀수 만큼 반복하여 가로
