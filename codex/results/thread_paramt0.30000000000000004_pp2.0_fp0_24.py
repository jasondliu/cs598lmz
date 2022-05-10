import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# Define the update function
def update(i):
    global x, y, x_new, y_new, x_old, y_old, x_new_old, y_new_old, x_new_new, y_new_new
    x_new_new = x_new_old + (x_new - x_old)
    y_new_new = y_new_old + (y_new - y_old)
    x_new_old = x_new
    y_new_old = y_new
    x_new = x_new_new
    y_new = y_new_new
    x_old = x
    y_old = y
    x = x_new
    y = y_new
    line.set_data(x, y)
    return line
