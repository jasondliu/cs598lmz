import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import sys
import os
import json
import time
import traceback
import threading
import multiprocessing
import queue
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patches as mpatches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMessageBox
import tkinter.filedialog as tkFileDialog
import tkinter.simpledialog as tkSimpleDialog
import tkinter.scrolledtext as tkScrolledText
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import scrolledtext
from PIL import Image, ImageTk

# 全局变
