import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import math

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GObject

from gi.repository import GdkPixbuf

from gi.repository import Pango

from gi.repository import Gio

from gi.repository import GLib

from gi.repository import GdkX11

from gi.repository import Gst

from gi.repository import GstVideo

from gi.repository import GstRtspServer

#from gi.repository import WebKit2

class Globals(object):
    debug = True
    debug_level = 1
    prog_version = "0.1"
    prog_name = "Pigeon-Cam"
    prog_description = "Pigeon Camera"
    app = None
    main_window = None

