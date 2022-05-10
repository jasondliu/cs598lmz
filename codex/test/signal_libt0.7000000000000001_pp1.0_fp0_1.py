import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk, Gdk, GdkPixbuf, GObject
import os, sys

