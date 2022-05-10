import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(ctypes.c_int(1))

import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import numpy as np
import pandas as pd

from skimage import io
from urllib.request import urlopen

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from io import BytesIO

font = 'C:/Windows/Fonts/Arial.ttf' # set this to match the font on your machine

labels = [
    'n02691156', 'airplane',
    'n02419796', 'antelope',
    'n02131653', 'bear',
    'n02834778', 'bicycle',
    'n01503061', 'bird',
    'n02924116', 'bus',
    'n02958343', 'car',
    'n02402425', 'cattle',
    'n02084071', 'dog',
    'n02
