import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import os.path
import subprocess
import time
import re
import datetime
import json
import urllib
import urllib2
import urlparse
import logging
import logging.handlers
import optparse
import ConfigParser
import threading
import traceback
import socket
import struct
import ctypes
import ctypes.util

from collections import defaultdict

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('GdkPixbuf', '2.0')
gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')
gi.require_version('GstApp', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gtk, Gdk, GdkPixbuf, Gst, G
