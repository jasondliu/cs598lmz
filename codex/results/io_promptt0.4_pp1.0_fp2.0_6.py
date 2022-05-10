import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno
import stat
import shutil
import random
import struct
import weakref
import threading

from test import test_support
from test.test_support import TESTFN, unlink, run_unittest

# Test the raw I/O classes from the io module.
# The tests are run with three different TextIOWrapper modes:
# - translating (the default), writing a newline as '\n'
# - untranslated: writing a newline as '\r\n'
# - universal newlines: writing a newline as '\r', '\n' or '\r\n'
# and with a number of different RawIOBase derived classes:
# - BytesIO
# - an in-memory stream
# - a stream that writes to a file
# - a stream that writes to a text file
# - a stream that writes to a socket
# - a stream that writes to a pipe
# - a stream that raises an IOError for every operation

# Decorator for skipping tests
