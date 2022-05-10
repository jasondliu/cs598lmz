import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)
import os
import cv2
import glob
import re
import Tkinter, tkFileDialog
import shutil
import string as st
import sys
import numpy as np
import matplotlib.pyplot as plt
import csv
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageChops
import math
import scipy.io as sio
import scipy
import pylab as pl
import PIL.ImageOps
import subprocess
from skimage import io, img_as_float, transform

import glob
import re

def getVideoLength(filepath):
    try:
        result = subprocess.Popen(["ffprobe", filepath],stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    except OSError:
        return 0
    
    secs = [0]
    
    for x in result.stdout.readlines
