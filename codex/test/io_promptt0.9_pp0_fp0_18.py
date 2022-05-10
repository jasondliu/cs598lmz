import io
# Test io.RawIOBase.readinto
import array
import math
import sys
from collections import namedtuple
from string import printable
from itertools import cycle, chain
from os import urandom
from unittest import mock
try:
    import threading
except ImportError:
    threading = None
try:
    import _testbuffer
except ImportError:
    _testbuffer = None


MAX_LEN = sys.maxsize # too slow when MAX_LEN = sys.maxsize
SMALLCHUNKS = [1, 8, 64, 1024, 1024 ** 2]
BIGCHUNKS = [2 ** i for i in range(30)] # 1G
