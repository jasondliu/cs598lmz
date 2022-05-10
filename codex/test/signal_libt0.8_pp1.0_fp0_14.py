import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import ui_main
from sys import platform
import serial.tools.list_ports
from RPi import GPIO
import spidev
from pynput.keyboard import Key, Listener, KeyCode
from xmodem import XMODEM, CRC
import os

class mySerial():
    def __init__(self, in_com, in_band, in_data, in_stop, in_parity, in_timeout):
        self.com = in_com
        self.band = in_band
        self.data = in_data
        self.stop = in_stop
        self.parity = in_parity
        self.timeout = in_timeout
        self.ser = serial.Serial()
