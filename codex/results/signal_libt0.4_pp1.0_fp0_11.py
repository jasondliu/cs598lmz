import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import subprocess
import traceback
import threading
import gettext
import locale
import logging
import logging.handlers
import json

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('GdkX11', '3.0')
gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')
gi.require_version('GstPbutils', '1.0')
gi.require_version('GstApp', '1.0')
from gi.repository import Gtk, Gdk, GdkX11, Gst, GstVideo, GstPbutils, GstApp

from . import utils
from .utils import get_pipeline_string
from .utils import get_pipeline_string_preview
from .utils import get_p
