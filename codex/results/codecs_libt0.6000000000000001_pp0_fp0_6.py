import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# from tkinter import *

# from tkinter import ttk

import tkinter as tk

# from tkinter import Tk, Frame, Entry, Label, Button, END, messagebox



# from tkinter import filedialog

from tkinter import filedialog

from tkinter import messagebox



import os

import sys

import datetime

import time

import pandas as pd

import numpy as np

import re



import matplotlib

matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from matplotlib.figure import Figure

from matplotlib import pyplot as plt



import matplotlib.dates as mdates

from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter



from mat
