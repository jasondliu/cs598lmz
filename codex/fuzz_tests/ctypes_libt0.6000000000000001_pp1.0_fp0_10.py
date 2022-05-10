import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import sys
import os
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib
import matplotlib.patches as patches
import matplotlib.cbook as cbook
import matplotlib.image as mpimg
from matplotlib.widgets import RadioButtons, Button, Slider, CheckButtons
from matplotlib.widgets import RectangleSelector
import matplotlib.patheffects as PathEffects
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

import cv2

import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")

import argparse

from tqdm import tqdm
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from skimage import color
