import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

import os
import sys
import json
import time
import datetime
import traceback
import threading
import webbrowser
import subprocess
import urllib
import fileinput
import shutil
import re
import zipfile
import requests
import atexit
import platform
import _winreg
import socket

from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import QUrl, QDir, QProcess, QThread, pyqtSignal, QSettings, QVariant, Qt
from PyQt4.QtGui import QDesktopServices, QMessageBox, QFileDialog, QListWidgetItem, QPixmap, QTextCursor, QTextDocument, QColor
from PyQt4.QtWebKit import QWebView, QWebPage

from requests_toolbelt import MultipartEncoder
from requests
