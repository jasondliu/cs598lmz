import bz2
bz2_file = bz2.BZ2File('/Users/susanaparis/Desktop/python-novice-inflammation/data/inflammation-01.csv.bz2')
print(bz2_file)

import glob
print(glob.glob('/Users/susanaparis/Desktop/python-novice-inflammation/*.csv'))

import os
print(os.getcwd())

import numpy
numpy.loadtxt(fname='/Users/susanaparis/Desktop/python-novice-inflammation/data/inflammation-01.csv', delimiter=',')

data = numpy.loadtxt(fname='/Users/susanaparis/Desktop/python-novice-inflammation/data/inflammation-01.csv', delimiter=',')
print(data)

print(type(data))

print(data.dtype)

print(data.shape)

print('first value in data:', data[0, 0])

print('middle value in data:', data[30
