import ctypes
import ctypes.util
import threading
import sqlite3
import math
import time
import sys
import os
import traceback

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GObject, GLib
import xpybutil
import xpybutil.ewmh
import xpybutil.event
import xpybutil.icccm
import xpybutil.util
import xpybutil.window

import util
import config

class WindowManager:
  """
    Main class that handles everything. A lot of this is based on the
    python-xlib example code.
  """

  def __init__(self):
    self.applications = {}
    self.applications_list = []
    self.desktop_layout = None
    self.desktop_manager = None
    self.desktop_manager_event_handler = None
    self.wm_name = "eclim WM"
    self.wm_class = "eclim WM"
    self.wm_pid = os.getpid()
