import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
from datetime import datetime

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject

from . import config


class GStreamerPipeline(object):
    """
    A simple class for controlling a GStreamer pipeline.

    The interface is intentionally made similar to that of
    GStreamer's own Pipeline class.
    """
    def __init__(self, pipeline_description):
        self.pipeline = Gst.parse_launch(pipeline_description)

    def get_by_name(self, name):
        return self.pipeline.get_by_name(name)

    def set_state(self, state):
        return self.pipeline.set_state(state)

    def get_state(self, timeout=Gst.CLOCK_TIME_NONE):
        return self.pipeline.get_state(timeout=timeout)

