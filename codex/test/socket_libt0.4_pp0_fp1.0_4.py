import socket
import sys
import time
import threading
import json
import random
import os

from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QFileDialog, QMessageBox
from PyQt5.QtWidgets import QWidget, QPlainTextEdit, QProgressBar, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView
from PyQt5.QtGui import QIcon, QFont, QBrush, QColor, QPixmap

from p2p_client import P2P_Client
from p2p_server import P2P_Server

# 文件分片大小
CHUNK_SIZE = 1024 * 1024 * 4

