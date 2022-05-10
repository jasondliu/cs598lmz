import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/home/li/temp/test.db")

import time, sys, os, shutil, mmap
import multiprocessing as mp
from multiprocessing import Pool
from multiprocessing import Process, Manager
import subprocess

from utils import *

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#from tkinter import *

import serial
# import serial.tools.list_ports
# print(serial.tools.list_ports.comports())

# HID 设备
# libhidapi = ctypes.cdll.LoadLibrary("./hidapi/libhidapi-libusb.so")
# libhidapi = ctypes.cdll.LoadLibrary(".
