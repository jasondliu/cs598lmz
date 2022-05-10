import mmap
import os
import re
import subprocess
import sys
import tempfile

import cv2
import numpy as np
import pytesseract
import requests
from PIL import Image
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def get_text(img):
    try:
        text = pytesseract.image_to_string(img)
    except Exception as e:
        print(e)
        text = ''
    finally:
        return text

def get_text_from_image(image):
    text = []
    d = pytesseract.image_to_data(image, output_type=Output.DICT)
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][
