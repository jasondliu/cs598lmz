import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import glob
import logging
import logging.handlers
import threading
import subprocess
import datetime
import traceback

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('GdkPixbuf', '2.0')
gi.require_version('GObject', '2.0')
gi.require_version('GLib', '2.0')
gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')
from gi.repository import GObject, Gst, GstVideo, GLib, Gtk, GdkPixbuf
GObject.threads_init()
Gst.init(None)

import config
import gui
import gui.utils
import gui.widgets
import gui.dialogs
import gui.dialogs.utils
import gui.dial
