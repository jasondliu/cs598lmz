import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()

from math import pi, sin, cos
from random import random
from PIL import Image

from PIL import Image

W, H = 700, 700
img = Image.new("RGB", (W, H))
pix = img.load()

def f(x, y):
    return sin(x) * cos(y)

def put_pixel(x, y, color):
    y = H - y - 1
    pix[x, y] = (color, color, color)

def draw_line(x1, y1, x2, y2):
    if abs(x1 - x2) > abs(y1 - y2):
        if x1 > x2:
            a, b = x2, y2
            x2, y2 = x1, y1
            x1, y1 = a, b
