import weakref
import logging
import threading
import time
import traceback
import sys
import os
import signal

from . import util

log = logging.getLogger(__name__)

class Task(object):
    """
    A task is a function that is executed in a separate thread.
    """
    def __init__(self, name, func, *args, **kwargs):
        self.name = name
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.thread = None
        self.running = False
        self.result = None
        self.exception = None
        self.traceback = None
        self.start_time = None
        self.end_time = None
        self.start_event = threading.Event()
        self.end_event = threading.Event()

    def __str__(self):
        return "<Task %s>" % self.name

    def __repr__(self):
        return "<Task %s>" % self.name

