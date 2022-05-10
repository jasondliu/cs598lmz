import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

import numpy as np

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

import csv

import scipy.optimize as opt

#import sys

#sys.path.append('../../scripts/')

from Tkinter import *
import tkFileDialog

numTimes = 9

numDays = 5

def convertDate(d):
	#starting from 203/10/1, convert the date to int
	M = { "Jan" : 1, "Feb" : 2, "Mar" : 3, "Apr" : 4, "May" : 5, "Jun" : 6, "Jul" : 7, "Aug" : 8, "Sep" : 9, "Oct" : 10, "Nov" : 11, "Dec" : 12}
	l = d.split("/")
	l = [int(x) for x in
