import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QThread, SIGNAL

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import pyglet
from pyglet.window import key
import pyglet.gl as gl

from math import sin, cos, pi
import numpy as np

import random

from time import time

from threading import Thread
from time import sleep

import argparse

from utils import *
from world import *
from model import *

from collections import deque


# Some global variables
args = {}
world = None
model = None

FPS = 60.0
dt = 0.0
last_time = 0.0

