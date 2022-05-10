import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import urllib
import urllib2
import subprocess
import platform
import datetime
import re
import json

from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets

from style_rc import *
from icons_rc import *
from main_ui import *
from settings import *
from about import *
from context_menu import *
from tabs_ui import *
from lists_ui import *
from lists_ui import *
from new_list_ui import *
from new_task_ui import *
from edit_task_ui import *
from edit_list_ui import *
from sync_ui import *

def get_resource(name):
    return os.path.join(os.path.dirname(__file__), name)
