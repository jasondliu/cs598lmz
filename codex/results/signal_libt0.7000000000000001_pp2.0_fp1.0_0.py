import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys
import time
import threading
import struct
import numpy as np
import can
import os
import pynmea2
import queue
from collections import deque
import struct
import math
from datetime import datetime
from can import Message

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QLabel, QLineEdit
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import scrolledtext
from math import sqrt
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QPen
from
