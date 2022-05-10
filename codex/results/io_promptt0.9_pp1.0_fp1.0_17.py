import io
# Test io.RawIOBase conformance.
# This is tested as part of the test_io test suite.
import os
import os.path
import pipes
import re
import signal
import socket
import stat
import struct
import sys
import tempfile
import threading
import unittest
import warnings
from test import support
from io import BytesIO, BufferedReader
from test.support import ThreadJoinTimeoutTest
from test.support import import_module, verbose, run_unittest, unlink
from test.support.script_helper import assert_python_ok, assert_python_failure
from test.support.test_helper import TestHandler

import _testbuffer

# _DEFAULT_CHUNK_SIZE: http://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader.readexactly
if sys.version_info[:2] >= (3, 4):
    _DEFAULT_CHUNK_SIZE = 65536
else:
    _DEFAULT_CHUNK_SIZE = -1

IS_PYPY = '__p
