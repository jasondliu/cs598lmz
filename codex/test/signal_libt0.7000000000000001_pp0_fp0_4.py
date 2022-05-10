import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from multiprocessing import Process, Queue
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from base import Settings
import cv2
import numpy as np
import time
from PIL import Image
from PIL import ImageTk
import threading

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import Tkinter as tk
import ttk
import math

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.unique_id = 0
        self.createWidgets()
