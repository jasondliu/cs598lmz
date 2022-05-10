import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

# Import the necessary packages
import numpy as np
import cv2
import time
import math
import sys
import os
import datetime
import argparse
import imutils
import glob
import serial
import serial.tools.list_ports
import threading
import time
import csv
import pandas as pd

# Import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
from imutils.video import WebcamVideoStream
from imutils.video import FileVideoStream
from imutils.video import FPS
from imutils import paths
from imutils.video import FileVideoStream
from imutils.video import FPS

# Import the necessary packages
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sk
