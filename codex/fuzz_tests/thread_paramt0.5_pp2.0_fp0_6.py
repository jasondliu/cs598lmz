import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import cv2
import time
import sys,os
import serial
import time
import math
import datetime
import logging
import logging.handlers
import requests
import json
import random

from scipy.interpolate import interp1d
from scipy.interpolate import Rbf

from utils.utils import *
from utils.colors import *
from utils.keypoints import *
from utils.process_config import *

from keras.models import load_model
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

global model
global graph
global sess
global graph2
global sess2
global graph3
global sess3
global graph4
global sess4
global graph5
global sess5
global graph6
global sess6
