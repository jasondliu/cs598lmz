import ctypes
import ctypes.util
import threading
import sqlite3
import os

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

import gettext
gettext.install("cinnamon", "/usr/share/locale")

import __builtin__
__builtin__._ = gettext.gettext

import xcursor

from util import *
from xsettings import XSettingsWatcher
from xrandr import XRandR

class WindowManager:
    def __init__(self):
        self.screen = None
        self.previous_workspace = -1
        self.current_workspace = -1
        self.dialogs = []
        self.dock = None
        self.dialog_group = None
        self.screen_saver_group = None
        self.override_group = None
        self.modal_dialog_group = None
        self.notifications_group = None
        self.last_active_workspace = None
        self.last_active_window = None
        self.last_workspace
