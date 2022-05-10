import socket
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QHBoxLayout
from PyQt5.QtCore import Qt, QThread, pyqtSignal

from pynput.keyboard import Key, Listener

# TODO:
# 1. При нажатии на кнопку должен запускаться поток для отправки клавиш (нажатие, отпускание)
# 2. Поток должен запускаться каждый раз при нажатии на кнопку

