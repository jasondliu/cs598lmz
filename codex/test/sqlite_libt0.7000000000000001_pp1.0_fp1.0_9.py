import ctypes
import ctypes.util
import threading
import sqlite3
import time
from http.server import *
from socketserver import *
from urllib.parse import urlparse, parse_qs

from gi.repository import Gtk
from gi.repository import GObject
from gi.repository import Gdk
from gi.repository import GLib

from . import update
from . import config
from . import xdg
from . import filechooser
from . import search

from .gtk_thread_safe import thread_safe_gtk, install_gtk_lock
from .logger import Logger
from .message_area import MessageArea
from .subprocess import *


_ = config.translation.gettext

log = Logger()


#------------------------------------------------------------------------------
#
# WindowController
#
#------------------------------------------------------------------------------

class WindowController(Gtk.Window):

    """
    Controller for the main window.
    """

    def __init__(self):

        Gtk.Window.__init__(self)

        self.create_gui()

