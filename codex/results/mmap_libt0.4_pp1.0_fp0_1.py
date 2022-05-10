import mmap
import os
import sys
import threading
import time

import pytest

from . import util

# On Windows, the default I/O mode is O_TEXT. Set this to O_BINARY
# to avoid unwanted modifications of the input data.
if 'b' not in open(__file__).read(1):
    O_BINARY = 0
else:
    O_BINARY = os.O_BINARY


def test_issue_5238():
    # On Windows, mmap.mmap(-1, 1) raises an exception.
    # It should succeed and map to the end of the file.
    f = open(TESTFN, 'wb')
    f.write(b'\0')
    f.flush()
    with open(TESTFN, 'rb') as f:
        m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_WRITE)
        assert m.size() == 1
        m.close()


def test_anonymous_maps_named():
    # Issue #11
