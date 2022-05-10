import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QGroupBox, QCheckBox, QFileDialog, QProgressBar
from PyQt5.QtCore import QCoreApplication
import sys
import os
import time
import cv2
import numpy as np
import threading
import queue
import subprocess
import json
import glob
import re
import copy
import shutil
import zipfile
import requests
import urllib.request
import ur
