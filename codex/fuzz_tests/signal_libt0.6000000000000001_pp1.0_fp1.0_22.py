import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QListWidget, QListWidgetItem, QErrorMessage, QMessageBox
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import QCoreApplication, QSize
from PyQt5.QtMultimedia import QSound
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

from PyQt5.QtGui import QColor

from PyQt5.QtCore import QUrl

from PyQt5.QtCore import QTimer

import sys
import os
import time
import random
import pickle
import threading


# Класс главного ок
