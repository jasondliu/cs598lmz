import mmap
import os
import sys
import string
import subprocess
import time
import numpy as np
import numpy.fft as nft
import scipy.fftpack as fft
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.ticker import MaxNLocator
from matplotlib.colors import LogNorm
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import OldScalarFormatter

#header information for binary files
header_size = 2048

#read from config file
with open("config.txt") as f:
    lines = f.read().splitlines()
    f.close()

#define data format
datatype = np.dtype(np.float32)

#set up data acquisition parameters

nx = int(lines[1]) #number of samples
ny = int(lines[3]) #number of shots

#read voltage data
data = np.zeros((ny,nx),dtype=datatype)

