from bz2 import BZ2Decompressor
BZ2Decompressor = BZ2Decompressor

import gzip
GzipFile = gzip.GzipFile

import os
import re
import stat

from . import _import

#------------------------------------------------------------------------------

# This is a reimplementation of the standard library's `shutil.copyfileobj`
# function, but it fixes an annoying bug in it.

def copyfileobj(fsrc, fdst, length=16*1024):
    """copy data from file-like object fsrc to file-like object fdst"""
    while 1:
        buf = fsrc.read(length)
        if not buf:
            break
        fdst.write(buf)

#------------------------------------------------------------------------------

class File(object):

    __slots__ = (
        '_fd',
        '_file_name',
        '_file_size',
        '_file_size_is_known',
        '_file_size_is_real',
        '_file_size_was_read',
        '_is_regular',
        '_opened',
        '_owns_fd',
