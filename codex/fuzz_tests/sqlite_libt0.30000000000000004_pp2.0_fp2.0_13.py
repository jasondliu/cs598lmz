import ctypes
import ctypes.util
import threading
import sqlite3

import os
import sys
import time
import datetime
import traceback
import subprocess

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GLib
from gi.repository import GObject

import config
import utils
import dbus
import dbus.service
import dbus.mainloop.glib
import dbus.glib

import logging
log = logging.getLogger("modules.MediaPlayer")

#------------------------------------------------------------------------

class MediaPlayer(dbus.service.Object):
    """
    Media Player module.
    """

    def __init__(self, session_bus, obj_path, module_config, content_box):

        self.session_bus = session_bus
        self.obj_path = obj_path
        self.module_config = module_config
        self.content_box = content_box
        self.player_name = module_config["player"]
        self
