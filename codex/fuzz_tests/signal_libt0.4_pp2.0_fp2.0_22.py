import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import logging
import argparse
import threading
import subprocess
import Queue
import traceback

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')
from gi.repository import Gtk, Gdk, Gst, GObject, GdkX11, GstVideo

from common import set_log_level
from common import set_log_file
from common import set_log_stdout
from common import set_log_color
from common import get_logger
from common import get_log_level
from common import get_log_file
from common import get_log_stdout
from common import get_log_color

from common import get_pipeline
from common import get_pipeline_string
from common import set_pipeline_string
from common import get_pip
