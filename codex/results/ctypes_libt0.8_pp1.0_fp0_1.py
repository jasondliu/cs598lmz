import ctypes
ctypes.cdll.LoadLibrary('libXt.so')
ctypes.cdll.LoadLibrary('libX11.so')
import Tkinter as tk
import ttk as ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.figimage import FigureImage
from matplotlib.image import imread
from matplotlib.widgets import RectangleSelector
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon
from matplotlib.patches import Ellipse
from matplotlib.patches import Circle

import numpy as np
import random as rd
import pickle

from skimage import io
from skimage.feature import hog
from skimage import data, exposure

from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin
from sklearn.datasets import load_
