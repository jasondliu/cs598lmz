import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

# Тут начинается программа

# Импортируем всё, что нужно
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QFileDialog, QInputDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, QTime
import datetime
import subprocess
import os
import time
import _thread
import threading
import re
import requests
import json
import pickle
import shutil

# Импортируем всё, что нужно для изменения ра
