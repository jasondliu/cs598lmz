import _struct
from _struct import *
from _struct import __doc__

# This module provides direct access to the internal structure module.
# Function names have been changed to avoid collisions with the Python
# module.

# Exports
__all__ = ["__doc__", "error", "Struct", "calcsize", "pack", "unpack", "pack_into", "unpack_from"]

# Types
Struct = _struct.Struct

# Functions
def calcsize(fmt):
    return _struct.calcsize(fmt)

def pack(fmt, *args):
    return _struct.pack(fmt, *args)

def unpack(fmt, string):
    return _struct.unpack(fmt, string)

def pack_into(fmt, buffer, offset, *args):
    return _struct.pack_into(fmt, buffer, offset, *args)

def unpack_from(fmt, buffer, offset=0):
    return _struct.unpack_from(fmt, buffer, offset)
