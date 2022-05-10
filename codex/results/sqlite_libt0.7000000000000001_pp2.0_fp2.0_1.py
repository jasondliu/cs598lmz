import ctypes
import ctypes.util
import threading
import sqlite3
import time

import logging
import os
import sys

import traceback

import logging

import pyinotify

import numpy

import pdb

class LoggingEventHandler(pyinotify.ProcessEvent):
    """Logs all the events captured."""
    def process_default(self, event):
        logging.info('%s of %s' % (event.maskname, event.pathname))

class FileCloseEventHandler(pyinotify.ProcessEvent):
    """Logs all the events captured."""
    def process_default(self, event):
        logging.info('%s of %s' % (event.maskname, event.pathname))

class CallbackEventHandler(pyinotify.ProcessEvent):
    #def __init__(self, time_diff):
    def __init__(self, time_diff, callback):
        #self.time_diff = time_diff
        self.callback = callback
        self.file_close_time = 0

    def process_default(self, event):
        logging.info('
