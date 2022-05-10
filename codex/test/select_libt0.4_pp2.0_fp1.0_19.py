import select
import socket
import sys
import time

# Importing the required modules
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QMainWindow, QFileDialog

from client import Client
from server import Server
from utils import *

# Global variables
global server
global client
global server_thread
global client_thread
global client_socket
global server_socket
global server_ip
global server_port
global client_ip
global client_port
global client_name
global server_name
global server_list
global client_list
global client_list_index
global server_list_index
global server_list_index_temp
global client_list_index_temp
global server_list_index_temp_
