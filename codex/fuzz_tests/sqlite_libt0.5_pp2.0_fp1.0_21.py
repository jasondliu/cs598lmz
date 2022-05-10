import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.kdeui import *
from PyKDE4.kdecore import *
from PyKDE4.kio import *
from PyKDE4.kparts import *
from PyKDE4.ktexteditor import *
from PyKDE4.ktexteditor import KTextEditor
from PyKDE4.ktexteditor import KTextEditor
from PyKDE4.ktexteditor import KTextEditor
from PyKDE4.ktexteditor import KTextEditor
from PyKDE4 import kdecore

from kate_core import *
from kate_settings import *
from kate_documents import *
from kate_view import *

import kate_plugin

class Kate(QObject):
    def __init__(self, parent=None, name=None, ctx=None):
        super(Kate, self).__init__(parent)
        self.ctx = ctx
        self.mainWindow
