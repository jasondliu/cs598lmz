import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QHeaderView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, QTimer, qInstallMessageHandler, QSettings
from server_ui import Ui_MainWindow
from server_worker import ServerWorker
from server_main import MainWindow
from server_config import ConfigWindow
from server_log_window import LogWindow
from server_stats_window import StatsWindow
from server_send_window import SendWindow
from server_about import AboutWindow
from server_help import HelpWindow
from server_send_to_all import SendToAllWindow
from server_log_edit import LogEditWindow
from server_stats_edit import StatsEditWindow
from server_helpers import *
from server_config_edit import ConfigEditWindow


# Класс главного окна
