import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

from PyQt5.QtCore import QThread, pyqtSignal
import time
import sys
import time
import os
import cv2
import numpy as np
import datetime
import threading
import requests
import json
import re
import random

from face_recognition import face_locations, face_encodings, compare_faces
from PIL import Image, ImageDraw

#from wxPython.wx import *
import wx

import requests
import json
import re
import random
import time

from face_recognition import face_locations, face_encod
