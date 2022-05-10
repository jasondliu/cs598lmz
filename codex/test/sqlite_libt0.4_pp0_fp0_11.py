import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import traceback

import numpy as np

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GObject, GdkPixbuf

import pygame
import pygame.camera

import cv2

# import matplotlib
# matplotlib.use('GTKAgg')
# import matplotlib.pyplot as plt

# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas
# from matplotlib.figure import Figure

# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas
# from matplotlib.figure import Figure

# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_gtk3 import FigureCanvasGTK3 as Figure
