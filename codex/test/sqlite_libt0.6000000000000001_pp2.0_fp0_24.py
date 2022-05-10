import ctypes
import ctypes.util
import threading
import sqlite3
import logging
import time
import re
import os
import sys

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

log = logging.getLogger(__name__)


class DNSQuery(ctypes.Structure):
    _fields_ = [("transaction_id", ctypes.c_ushort),
                ("flags", ctypes.c_ushort),
                ("questions", ctypes.c_ushort),
                ("answer_rrs", ctypes.c_ushort),
                ("authority_rrs", ctypes.c_ushort),
                ("additional_rrs", ctypes.c_ushort),
                ("queries", ctypes.c_ubyte * 1)]

    def __init__(self, data):
        super(DNSQuery, self).__init__()
        self.parse(data)

    def parse(self, data):
        ctypes.memmove(ctypes.addressof(self), data, ctypes.sizeof(self))


