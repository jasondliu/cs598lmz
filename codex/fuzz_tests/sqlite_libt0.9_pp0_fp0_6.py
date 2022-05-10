import ctypes
import ctypes.util
import threading
import sqlite3
import time
import datetime
import sys
import os
import psutil
import multiprocessing
import subprocess
import json

try:
    import argparse
except ImportError:
    import argparse

import google

try:
    import gi

    gi.require_version('AppIndicator3', '0.1')
    gi.require_version('Gtk', '3.0')
except (ImportError, ValueError):
    print('Missing gi.repository.Gtk or appindicator3')
    sys.exit()

from gi.repository import Gtk
from gi.repository import GObject
from gi.repository import AppIndicator3 as appindicator

from requests.exceptions import HTTPError
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# App info
APPINDICATOR_ID = 'myappindicator'

# Log paths
WHITE_LIST_DB_LOG = os.path.abspath(os.path.join(
    os.path
