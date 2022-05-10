import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import time

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('GdkPixbuf', '2.0')
gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')
gi.require_version('GstApp', '1.0')
gi.require_version('GstRtspServer', '1.0')

from gi.repository import GObject, Gst, Gtk, Gdk, GdkPixbuf, GstVideo, GstApp, GstRtspServer

# Needed for window.get_xid(), xvimagesink.set_window_handle(), respectively:
from gi.repository import GdkX11, GstXv

# Needed for window.get_xid(), xvimagesink.set_window
