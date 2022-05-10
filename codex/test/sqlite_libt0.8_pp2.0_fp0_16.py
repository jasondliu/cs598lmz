import ctypes
import ctypes.util
import threading
import sqlite3
import os
import re
import subprocess
import sys
import weakref

from dbus.mainloop.glib import threads_init as dbus_threads_init
dbus_threads_init()
from gi.repository import GLib as glib

_libhal = None
_hal_context = None
_hal_devices = None
_hal_ignore_unmounted_interfaces = None

def get_hal_context():
    global _libhal
    global _hal_context
    global _hal_devices
    global _hal_ignore_unmounted_interfaces
    if _libhal is None:
        if 'DISABLE_HAL' in os.environ:
            return None
        _libhal = ctypes.CDLL(ctypes.util.find_library('hal'), use_errno=True)
    if _hal_context is None:
        _hal_context = _libhal.libhal_ctx_new()
        ret = _libhal.libhal_ctx_init(_hal_context, None)
