import socket
import sys
import time

from PIL import Image
import pytesseract
import cv2

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from pathlib import Path

import pyscreenshot as ImageGrab

import numpy as np

def get_ip():
    return socket.gethostbyname(socket.gethostname())

def get_port():
    return sys.argv[1]

def get_url():
    return sys.argv[2]

def get_driver():
    options = Options()
    options.headless = True
    return webdriver.Firefox(options=options)

def get_tesseract_config():
    return ('--oem 1 --psm 7 -c tessedit_char_whitelist=0123456789')

def get_captcha_path():
    return 'captcha.png'

def get_captcha_box():
    return (1170, 675, 1310, 710)

