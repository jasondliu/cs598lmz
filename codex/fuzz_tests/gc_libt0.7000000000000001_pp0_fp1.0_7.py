import gc, weakref
from collections import Counter
from random import choice
import random
import sys
import time
import threading

# for visualizing
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

# for GUI
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import tkinter.messagebox
import tkinter.filedialog

# for saving/loading
import pickle

# for animating GIF
import imageio

'''
현재 프로그램이 설치된 위치를 저장한다.
'''
CURRENT_PATH = os.getcwd()

'''
시뮬레이션이 진행되는 맵의 크기를
