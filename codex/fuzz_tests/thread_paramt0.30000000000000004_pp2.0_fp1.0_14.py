import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random

# create a random walker
class Walker:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.step = 0
        self.dir = random.randint(0,3)

    def move(self):
        if self.dir == 0:
            self.x += self.size
        elif self.dir == 1:
            self.y += self.size
        elif self.dir == 2:
            self.x -= self.size
        else:
            self.y -= self.size
        self.step += 1
        if self.step > 3:
            self.dir = random.randint(0,3)
            self.step = 0

# create
