import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
import struct
import os
import platform

from ctypes import c_void_p, c_int, c_char_p, c_long

import logging
log = logging.getLogger(__name__)

# ptypes
PTYPE_NONE = 0
PTYPE_NODE = 1
PTYPE_RELATION = 2
PTYPE_WAY = 3
PTYPE_AREA = 4

# key_val
KV_FLAG_DELETE = 0x20
KV_FLAG_ATTR = 0x80

class AttributeDict(dict):
    """A dictionary that allows for obj.key access to the dictionary entries."""
    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        self[name] = value

class Node(AttributeDict):
    def __init__(self, id, lat, lon):
        super(Node, self).__init
