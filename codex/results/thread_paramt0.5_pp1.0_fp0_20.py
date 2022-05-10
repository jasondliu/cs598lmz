import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

# import the necessary packages
from pyimagesearch.tempimage import TempImage
from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse
import warnings
import datetime
import imutils
import json
import time
import cv2
import os
from time import sleep
from skimage.measure import compare_ssim
from imutils import contours
from imutils import perspective
from scipy.spatial import distance as dist
import numpy as np
import imutils
import cv2
from pyzbar import pyzbar
from PIL import Image
from PIL import ImageEnhance
import numpy as np
import time
import sqlite3
import threading
import serial
import sys
import os
import RPi.GPIO as GPIO
import time
import picamera
import requests
import json
import io
import base64
import re
import math

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add
