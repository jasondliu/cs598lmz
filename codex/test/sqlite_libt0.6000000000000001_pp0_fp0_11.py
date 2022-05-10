import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys

from pprint import pprint

import gi
gi.require_version('Gst', '1.0')
from gi.repository import GObject, Gst, GstVideo
GObject.threads_init()
Gst.init(None)

#Gst.debug_set_active(True)
#Gst.debug_set_default_threshold(3)

import logging
logger = logging.getLogger(__name__)

import config

class GStreamerPipeline(object):

    def __init__(self, pipeline_desc):
        self.pipeline = Gst.parse_launch(pipeline_desc)
        self.bus = self.pipeline.get_bus()
        self.bus.add_signal_watch()
        self.bus.connect("message", self.on_message)

    def on_message(self, bus, message):
        t = message.type
        if t == Gst.MessageType.EOS:
            self.pipeline.set_
