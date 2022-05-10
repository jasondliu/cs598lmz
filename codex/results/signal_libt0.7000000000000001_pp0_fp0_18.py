import signal
signal.signal(signal.SIGINT, signal.SIG_DFL) # SIGINTを送ってもプロセスが終了しない

# 各ライブラリのインポート
import os
import sys
import cv2
import glob
import time
import random
import base64
import argparse
import numpy as np

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt

from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMainWindow
import qtawesome

from keras.models import model_from_json

from one_hot import onehot_to_class
from one_hot import class_to_onehot

from datetime import dat
