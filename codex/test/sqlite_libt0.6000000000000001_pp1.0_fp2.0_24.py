import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time

from ctypes import *

# Я не понимаю почему, но необходимо импортировать оба пакета, в противном
# случае не будет найден класс.
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst

Gst.init(None)

class GstPipeline(object):
    def __init__(self):
        self.pipeline = Gst.Pipeline()
        self.bus = self.pipeline.get_bus()
        self.bus.add_signal_watch()
        self.bus.connect("message", self.on_message)

