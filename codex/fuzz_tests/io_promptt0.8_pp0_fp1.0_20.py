import io
# Test io.RawIOBase implementation

import os
import unittest
from test import support
# Needed by test_ioctl
import fcntl
import struct

# test_ioctl must be tested before test_RawIOBase (at least on Linux),
# because test_ioctl changes the terminal attributes, and test_RawIOBase
# cares about them.

#
# Utility functions
#

# We need some special files for the test_ioctl tests:
#  - a terminal in cooked mode, to play with termios
#    (os.ctermid() can be used to get such a file)
#  - a FIFO, to check that ioctl works on pipes (os.mkfifo() can create
#    one, but that function may fail on some platforms)
CTERMID_WORKS=1
try:
    ctermid_fd=os.open(os.ctermid(), os.O_RDWR)
except (AttributeError, OSError):
    CTERMID_WORKS=0

def make_fifo(filename):
    try:
        os
