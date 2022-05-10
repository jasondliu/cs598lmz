import mmap
import os
import sys

from functools import cmp_to_key

#import qt_app
import qt_app

from PyQt5.QtCore import Qt, QFileInfo, \
                         QPoint, QSize, QUrl, QFile, QIODevice, \
                         QThread, pyqtSignal, \
                         QMutex, QMutexLocker, QTimer, QDateTime

from PyQt5.QtGui import QIcon, QScreen, QGuiApplication

from PyQt5.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu, QAction, QFileDialog, QMessageBox, QStyle

from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings, QWebEngineProfile

from PyQt5.QtNetwork import QNetworkRequest, QNetworkReply

class Progress:
    def __init__(self, main_window):
        self.main
