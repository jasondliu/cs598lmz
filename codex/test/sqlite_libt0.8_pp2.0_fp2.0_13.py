import ctypes
import ctypes.util
import threading
import sqlite3
import logging
import gc
import importlib

import wx
import wx.adv
import wx.lib.scrolledpanel as scrolled

log_handler = logging.StreamHandler(sys.stdout)
log_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))

logger = logging.getLogger('Crymet')
logger.addHandler(log_handler)
logger.setLevel(logging.DEBUG)

# Auto-update function
import urllib.request
import subprocess

