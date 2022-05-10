import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import time
import logging
import argparse
import threading
import subprocess

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('GdkPixbuf', '2.0')
gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')
gi.require_version('GstApp', '1.0')
from gi.repository import GObject, Gst, Gtk, Gdk, GdkPixbuf, GstVideo, GstApp

from lib.config import Config
from lib.utils import get_file_dir
from lib.utils import get_image_path
from lib.utils import get_video_path
from lib.utils import get_audio_path
from lib.utils import get_icon_path
from lib.utils import get_ui_file
