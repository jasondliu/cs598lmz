import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import re
import time
import datetime
import threading
import subprocess
import traceback
import logging
import logging.handlers
import json
import shutil

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('GdkPixbuf', '2.0')
gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')
gi.require_version('GstApp', '1.0')
from gi.repository import GObject, Gtk, Gdk, GdkPixbuf, Gst, GstVideo, GstApp

GObject.threads_init()
Gst.init(None)

import config
import util
import ui
import ui.widgets
