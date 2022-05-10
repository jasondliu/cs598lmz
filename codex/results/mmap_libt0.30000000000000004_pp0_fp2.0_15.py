import mmap
import re
import sys
import time
from datetime import datetime
from os import path
from subprocess import Popen, PIPE
from threading import Thread
from time import sleep
from typing import List, Dict, Tuple

import psutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, QThread
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QLineEdit, QMessageBox, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.uic.properties import QtGui
from PyQt5.QtGui import QFont

from src.utils import *
from src.utils.utils import *
from src.utils.utils import get_file_name_from_path
from src.utils.utils import get_file_path_from_path
from src.
