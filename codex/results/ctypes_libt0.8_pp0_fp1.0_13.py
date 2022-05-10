import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import sys, os, glob
sys.path.append('../tools')
from PIL import Image
from dotenv import load_dotenv
from dicom_tools import DicomTools
from dicom_convert import DicomConvert
from box_intersection_over_union import BoxIOU
from data_augmentation import DataAugmentation
from plot3d_tools import Plot3dTools
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pydicom
import random
import datetime
import time
import copy
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from plotly.colors import n_colors
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff

def get_bounding_box_info(dataframe
