import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randint

from bresenham import bresenham
from tkinter import *

root = Tk()

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def get_lines():
    lines = []
    for i in range(randint(1, 10)):
        x1 = randint(0, 10)
        y1 = randint(0, 10)
        x2 = randint(0, 10)
        y2 = randint(0, 10)
        lines.append(Line(x1, y1, x2, y2))
    return lines

def get_
