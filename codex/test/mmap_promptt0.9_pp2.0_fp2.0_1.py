import mmap
# Test mmap.mmap() max_len argument
import os
import errno
import unittest
from test import support

def _get_offset(fd):
    offset = mmap.ALLOCATIONGRANULARITY * 2 ** 6
    while True:
        try:
            fd.seek(offset)
            break
        except IOError as err:
            if err.errno != errno.EINVAL:
                raise
            offset >>= 1
    fd.write(b'\0')
    return offset

