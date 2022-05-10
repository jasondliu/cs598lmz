import mmap
import numpy as np

from matplotlib import pyplot as plt
from matplotlib import cm
from pylab import *

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LogNorm

import matplotlib.animation as animation

import subprocess
import os

from struct import *

def read_data_file(filename):
    #print(filename)
    f = open(filename, 'r')
    filedata = f.read()
    f.close()
    lines = filedata.split('\n')
    i = 0
    for line in lines:
        if line.startswith('#'):
            if line.startswith('# Number of particles'):
                N = int(line.split(': ')[1])
            if line.startswith('# Number of dimensions'):
                D = int(line.split(': ')[1])
