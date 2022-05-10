import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.animation as animation
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

from PIL import Image, ImageTk

from tqdm import tqdm
import time
from threading import Thread

import tensorflow as tf
import pyrealsense2 as rs

from Data_reader import Data_reader
from Network import Network

from Dataset_Creator import Dataset_creator
from CNN_Creator import CNN_Creator
from CNN_Trainer import CNN_Trainer
from CNN_Tester import CNN_Tester
from CNN_Loader import CNN_Loader

import numpy as np
import cv2

import os
import sys

import os.path
from os import
