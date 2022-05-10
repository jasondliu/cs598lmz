import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
import socket, asyncore
import sys, os, errno
import random
import re

import libtorrent as lt

from PyQt4.QtCore import Qt, QTimer, QThread, SIGNAL, QByteArray
from PyQt4.QtCore import QPoint, QUrl, QVariant
from PyQt4.Qt import QString, QClipboard
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *

from libtorrent import bencode
from libtorrent import bdecode

if sys.platform == "win32":
    import win32api
    import win32file
    import pywintypes

def fromUtf8(text):
    """Convert from utf-8 to unicode"""
    return unicode(QString.fromUtf8(text))

def toUtf8(text):
    """Convert from unicode to utf-8"""
    return QString(text).toUtf8()

_translate = Q
