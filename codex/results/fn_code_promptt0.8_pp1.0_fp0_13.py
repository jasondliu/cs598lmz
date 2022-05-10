fn = lambda: None
# Test fn.__code__.co_filename fails under py2exe
try:
    fn.__code__.co_filename
except AttributeError:
    import pythoncom
    pythoncom.CoInitialize()

import wx
import wx.lib.agw.ultimatelistctrl as ULC
from wx.lib.agw.toasterbox import TB_SIMPLE, TB_COMPLEX, ToasterBox

from wx.lib.pubsub import pub as Publisher

import threading
import os
import os.path
import sys
import ctypes, ctypes.wintypes
import win32con
import time

from nvpy.settings import appdir, get_config
from nvpy.notebook import NoteBook

from nvpy.notelist import *
from nvpy.tray import TrayIcon
from nvpy.prefs import NVPrefsDialog

from nvpy.winsync import sync_notes
from nvpy.winsync import sync_thread
from nvpy.winsync import sync_errors

from nvpy.utils import get_app_
