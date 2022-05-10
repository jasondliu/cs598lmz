import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import re
import sys
import pandas as pd
import numpy as np

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

def get_image_text(image_path):
    image_text = ocr_core(image_path)
    return image_text

def get_image_text_list(image_path_list):
    image_text_list = []
    for image_path in image_path_list:
        image_text = get_image_text(image_path)
        image_text
