import ctypes
import ctypes.util
import threading
import sqlite3
import os
import subprocess
import sys
import binascii
import re
import time
import traceback
import logging
import tempfile
import shutil
import socket
import fcntl
import struct

from . import util
from . import config
from . import __version__ as version

logger = logging.getLogger(__name__)

try:
    import dbus
except ImportError:
    dbus = None

try:
    import dbus.service
except ImportError:
    dbus.service = None

try:
    import dbus.mainloop.glib
except ImportError:
    dbus.mainloop.glib = None

try:
    import glib
except ImportError:
    glib = None

try:
    import gobject
except ImportError:
    gobject = None

try:
    import pygobject
except ImportError:
    pygobject = None

try:
    import pkg_resources
except ImportError:
    pkg_resources = None

try:
    import gi
