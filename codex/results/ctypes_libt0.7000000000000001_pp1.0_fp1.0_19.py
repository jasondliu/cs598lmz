import ctypes
ctypes.cdll.LoadLibrary("libc.so.6")
ctypes.CDLL("libc.so.6")

import matplotlib.pyplot as plt
import numpy as np

#example with 2 dimensios

sample1 = np.genfromtxt('1.csv', delimiter=',', skip_header=1)
sample2 = np.genfromtxt('2.csv', delimiter=',', skip_header=1)
sample3 = np.genfromtxt('3.csv', delimiter=',', skip_header=1)
sample4 = np.genfromtxt('4.csv', delimiter=',', skip_header=1)
sample5 = np.genfromtxt('5.csv', delimiter=',', skip_header=1)
sample6 = np.genfromtxt('6.csv', delimiter=',', skip_header=1)
sample7 = np.genfromtxt('7.csv', delimiter=',', skip_header=1)
sample8 = np.genfromtxt('8.csv', delimiter=',', skip_header=1)
