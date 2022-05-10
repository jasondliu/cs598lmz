import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import json
import logging
import threading
import multiprocessing
import traceback

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QFileDialog
from PyQt5.QtCore import QCoreApplication, QObject, QThread, pyqtSignal, pyqtSlot, QTimer, QDateTime, QIODevice, QByteArray
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

from . import config

logger = logging.getLogger(__name__)

# TODO:
#
# - Add support for more than one serial port
# - Add support for more than one serial baud rate
# - Add support for more than one serial data format
# - Add support for more than one serial flow control
# - Add support for more than one serial parity
# - Add support for more than one serial stop bits
# - Add support for more than one serial timeout
#
