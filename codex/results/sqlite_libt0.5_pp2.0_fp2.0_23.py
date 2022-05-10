import ctypes
import ctypes.util
import threading
import sqlite3
from time import sleep

from PyQt5.QtCore import QThread, pyqtSlot, pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap

from ui_mainwindow import Ui_MainWindow
from ui_infodialog import Ui_InfoDialog
from ui_aboutdialog import Ui_AboutDialog
from ui_settingsdialog import Ui_SettingsDialog
from ui_logdialog import Ui_LogDialog

from config import Config
from log import Log
from db import DB
from pihole import PiHole
from dnsmasq import Dnsmasq
from updater import Updater

from utils import get_ip, get_mac, get_hostname, get_gateway, get_dns_server, get_version
from utils import is_connected, is_ip, is_mac, is_hostname, is_gateway, is_dns_server, is_port
