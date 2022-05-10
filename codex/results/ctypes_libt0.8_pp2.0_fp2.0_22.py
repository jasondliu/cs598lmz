import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("WvdH.Cafetaria")
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import qdarkstyle

app = QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet())

import os
import logging
import logging.config

import datetime
import json
import xml.etree.ElementTree as et
import openpyxl

import mainwindow
import aboutdialog
import settingsdialog
import statusdialog
import splashdialog
import errordialog
import errorreport
import orderdialog
import ordersave
import ordersavecsv
import orderload
import orderloadxml
import orderloadjson
import orderloadxml
import orderloadjson
import orderloadcsv
import orderloadxlsx
import emailsend
import emailsendhtml
import emailsendtext
import emailsendcsv

import cafed
