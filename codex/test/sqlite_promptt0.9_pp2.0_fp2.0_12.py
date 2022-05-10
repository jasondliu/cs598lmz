import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:run/book.db3?mode=rwc', uri=True)
import signal
import select
import queue
import socket
import atexit
import os
import logging
import re
import sys
import time
import subprocess
import copy
import traceback

# https://docs.python.org/3.7/library/queue.html?highlight=queue
# https://docs.python.org/3.7/library/queue.html#queue.Queue.task_done
# https://docs.python.org/3.7/library/select.html?highlight=select
# http://man7.org/linux/man-pages/man7/signal.7.html

appName = "py2"

logging.basicConfig(level=logging.DEBUG,
  format='%(asctime)s %(levelname)s [%(threadName)s] %(name)s.%(funcName)s: %(message)s')

logger = logging.getLogger(__name__)

# UGLY - global gst
