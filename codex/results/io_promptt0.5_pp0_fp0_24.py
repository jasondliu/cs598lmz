import io
# Test io.RawIOBase

import unittest
from test import support

import io
import os
import sys
import time
import errno
import _thread
import random
import struct
import select
import socket

from io import BlockingIOError
from io import UnsupportedOperation

# Some tests check that operations block.  The tests are skipped if
# the platform has no way to wait for I/O completion.
HAVE_GET_EVENT_LOOP = hasattr(select, 'get_event_loop')

# Some tests check that operations block.  The tests are skipped if
# the platform cannot wait for I/O completion.
HAVE_POLL = hasattr(select, 'poll')

# Some tests check that operations block.  The tests are skipped if
# the platform cannot wait for I/O completion.
HAVE_SELECT = hasattr(select, 'select')

# Some tests check that operations block.  The tests are skipped if
# the platform cannot wait for I/O completion.
HAVE_EPOLL = hasattr(select, 'epoll')

# Some tests check that operations block.
