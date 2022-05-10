import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\r                   \r'), daemon=True).start()

import numpy as np
import pandas as pd
import cv2
import tkinter as tk
from PIL import Image, ImageTk
import argparse
import os
import shutil

from train import load_data, load_model, predict_single, load_thresholds, get_geometry

# Initialisation
sauv = './images/sauv.png'
notsauv = './images/notsauv.png'
border = '#f1d267'

geometry = get_geometry()
classes = os.listdir('./train/data/')
classes.sort()
image_size = 80

row_offset = 70
col_offset = 80

width = col_offset + image_size*len(classes) + col_offset
height = row_offset + image_size*2 + row_offset

# Set up GUI
window = tk.Tk()
window.title('Predicting...')
window.ge
