import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf, GObject

