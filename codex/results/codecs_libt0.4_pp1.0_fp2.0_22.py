import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import os
import sys
import logging
import logging.handlers
import time
import subprocess
import re
import datetime
import socket
import json
import urllib2
import base64
import random
import shutil
import ctypes
import traceback
import platform
import zipfile
import ConfigParser

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from PyQt4.QtNetwork import *
from PyQt4.QtCore import pyqtSlot as Slot

from ui_mainwindow import Ui_MainWindow
from ui_settings import Ui_Settings
from ui_about import Ui_About
from ui_login import Ui_Login
from ui_register import Ui_Register
from ui_register_success import Ui_RegisterSuccess
from ui
