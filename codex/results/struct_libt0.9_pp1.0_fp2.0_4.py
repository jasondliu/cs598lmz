import _struct
import codecs
import marshal
import os
import pprint
import struct
import sys
import time
import warnings

from idlelib import tooltip as tt


def is_byte_offset(offset):
    # For backwards compatibility reasons, IDLE 2.6 will use either
    # an integer or a string as the offset, depending on whether the
    # cache data is from the old or the new code.
    if isinstance(offset, int):
        return True
    try:
        offset + 0
    except TypeError:
        return False
    return True


class Cache:

    message = ('IDLE extension Trinket Symbol Browser is unable to '
               'run with this version of IDLE.\nTry upgrading to Python 3.0 '
               'or later.')

    def __init__(self, idlever=1):
        try:
            self.message = self.message
        except UnicodeDecodeError:
            self.message = 'IDLE Symbol Browser unable to run on this version'
        self.idlever = idlever
        self.cached_files = []
