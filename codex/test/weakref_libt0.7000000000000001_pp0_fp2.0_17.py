import weakref
import time
import ctypes
from ctypes import wintypes
import win32process
import win32api
import win32con
import win32security
import win32event
import win32job
import win32gui
import win32ts
import win32pipe

import augeas
import yaml

from gevent import select, Greenlet
from gevent.event import AsyncResult, Event
from gevent.queue import Queue
from gevent.threadpool import ThreadPool
from gevent.subprocess import Popen, PIPE


logger = logging.getLogger(__name__)


class GreenletTimeout(Exception): pass


def greenlet_wait(greenlet, timeout=None):
    if greenlet.ready():
        return greenlet.value
    # threadpool's greenlets do not expose their timer
    if hasattr(greenlet, 'timer'):
        timer = greenlet.timer
    else:
        timer = None
    if timeout is not None:
        if timer is not None:
            timer.cancel()
