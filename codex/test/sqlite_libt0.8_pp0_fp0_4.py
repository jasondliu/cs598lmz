import ctypes
import ctypes.util
import threading
import sqlite3
import os
import copy
import re
import time
import math
import logging
import subprocess

try:
    import xml.etree.cElementTree as etree
except ImportError:
    import xml.etree.ElementTree as etree

import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstBase', '1.0')
gi.require_version('GstVideo', '1.0')
gi.require_version('Gtk', '3.0')
from gi.repository import GObject, Gst, GstBase, GstVideo, GdkX11, Gtk

# set these for forking to work
Gst.init(None)
Gtk.init(None)

# Example from https://gstreamer.freedesktop.org/data/doc/gstreamer/head/gstreamer/html/Gstreamer-Base-Sinks.html#GstBaseSink-virtual-methods
