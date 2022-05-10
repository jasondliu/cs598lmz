import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import re
import time
import datetime
import subprocess
import threading
import traceback
import math

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('GdkPixbuf', '2.0')
gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')
gi.require_version('GstPbutils', '1.0')
from gi.repository import Gtk, Gdk, GdkPixbuf, Gst, GstVideo, GstPbutils

import config
import utils
import widgets
import dialogs
import gstplayer
import gstrecorder
import gstmixer
import gstpipeline
import gstutils
import gst_elements
import gst_elements_extra
import gst_elements_bad
