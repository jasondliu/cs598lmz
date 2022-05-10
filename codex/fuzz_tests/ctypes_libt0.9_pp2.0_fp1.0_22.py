import ctypes
ctypes.cdll.LoadLibrary("/usr/lib/x86_64-linux-gnu/libX11.so.6")
ctypes.cdll.LoadLibrary("/usr/lib/x86_64-linux-gnu/libXext.so.6")

import tkinter as tk; 
import tkinter.filedialog as fileDialog;
from PIL import Image, ImageDraw, ImageTk;
import cv2, os;
import numpy as np;
import tensorflow as tf;
import tensorflow.keras as keras;
import glob;
import matplotlib.pyplot as plt
from matplotlib.image import imread
import re;
import time;

# AI网络
modelSaveFile='./models/HSVFilterKanjia_A02_v1_T30_50_60_1571199672.h5';
model=keras.models.load_model(modelSaveFile);

videoFile=None;
labelNames_weishi=['肥皂','洗
