import ctypes
ctypes.windll.shell32.IsUserAnAdmin()

import os
import sys
import uuid
import json
import subprocess
import webbrowser
from datetime import datetime
from quamash import QEventLoop, QApplication
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWebChannel import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
from dropbox import client, rest, session
from PyQt5 import sip


class MyDropboxClient(QObject):
	'''
	MyDropboxClient is the python front end for accessing Dropbox.
	It allows you to get dropbox folder's content, upload files and download them.
	'''
	def __init__(self, parent
