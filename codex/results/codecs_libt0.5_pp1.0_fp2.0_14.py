import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import sys, os, time, re, requests, json, urllib
import argparse

from bs4 import BeautifulSoup
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QLabel, QLineEdit, QMessageBox, QInputDialog, QFileDialog, QProgressBar
from PyQt5.QtCore import pyqtSlot, Qt, QThread, QObject, pyqtSignal

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Bilibili下载器'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle
