import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import subprocess

from pylab import *
from matplotlib.pyplot import *
import numpy as np

def execute(command):
    popen = subprocess.Popen(command, stdout=subprocess.PIPE)
    lines_iterator = iter(popen.stdout.readline, b"")
    for line in lines_iterator:
        print(line)

def read_file(filename):
    y = []
    x = []
    first = True
    with open(filename, 'r') as f:
        for line in f.readlines():
            if first:
                first = False
                continue
            x.append(float(line.split(" ")[0]))
            y.append(float(line.split(" ")[1]))
    return x, y

def calc_gain(x, y):
    dc = y[0]
    peak = y[-1]
    return 20.0*log
