import select
import socket
import sys
import threading
import time

import cv2
import numpy as np
from PIL import Image
from PIL import ImageTk

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from threading import Thread

from camera_gui.main_gui import Ui_MainWindow
from camera_gui.setting_gui import Ui_Dialog

from utils.camera_utils import Camera
from utils.camera_utils import CameraCapture
from utils.camera_utils import Camera_Detector
from utils.camera_utils import Camera_Frame
from utils.camera_utils import Camera_Streaming
from utils.camera_utils import Camera_VideoWriter
from utils.camera_utils import Camera_VideoWriter_Thread

from utils.socket_
