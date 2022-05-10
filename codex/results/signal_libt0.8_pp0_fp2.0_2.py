import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys

from PySide2.QtCore import QCoreApplication, QObject, Slot, Signal, QRunnable, QThreadPool

from PySide2.QtQuick import QQuickView
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QLabel, QSizePolicy, QGridLayout, QPushButton, QBoxLayout
from PySide2.QtCore import QUrl, Property, Signal, QTimer, QRunnable, QThreadPool, QObject, Slot, QCoreApplication, QSize,QPoint
from PySide2.QtGui import QGuiApplication, QPixmap
from PySide2.QtWidgets import QApplication, QWidget, QPushButton
from PySide2 import QtCore

import threading

import time

from functools import partial

from .mainwindow_res import *

from .motor_widget import *
from .move_absolute_widget import *
from .move
