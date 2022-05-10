import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QUrl, QObject, QThread, pyqtSignal, pyqtSlot, QTimer
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QGuiApplication

import sys
import os
import time

from datetime import datetime

import threading

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

from PyQt5.QtCore import QUrl, QObject, QThread, pyqtSignal, pyqtSlot, QTimer
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QGuiApplication


