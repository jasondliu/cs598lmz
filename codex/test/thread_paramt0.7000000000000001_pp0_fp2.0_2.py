import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.Qt import QFont
import math
from threading import Thread
from threading import Event
from threading import Lock
import os
import time
import random
from timeit import default_timer as timer

import socket
import sys
import struct
import time
import random
from timeit import default_timer as timer

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtCore import pyqtSlot
import cv2
