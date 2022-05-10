import select
import time
import sys
import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as mdates
import datetime
from datetime import timedelta
from matplotlib.dates import DateFormatter

# set up serial port
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

# set up plot
fig, ax = plt.subplots()
ax.set_xlim(left=0, right=10)
ax.set_ylim(bottom=0, top=10)
ax.set_xlabel('Time')
ax.set_ylabel('Temperature')

# set up animation
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []

def init():
    line.set_data([], [])
    return line,

def run(data):
    # update the data
    t, y = data

