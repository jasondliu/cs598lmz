import ctypes
import ctypes.util
import threading
import sqlite3
import tempfile
import os
import time
import signal
import sys

from . import core_ffi, ffi
from .core import LLCommand, int_to_string, string_to_int

class USBContext(object):
    def __init__(self):
        self._ctx = core_ffi.lib.usb_context_new()
        if self._ctx == ffi.NULL:
            raise RuntimeError("Unable to create USB context")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.free()

    def free(self):
        assert self._ctx != ffi.NULL
        core_ffi.lib.usb_context_free(self._ctx)
        self._ctx = ffi.NULL

class USBDevice(object):
    def __init__(self, ctx, instance):
        self._ctx = ctx
        self._instance = instance

