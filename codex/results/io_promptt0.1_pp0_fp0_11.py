import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno
import weakref
import gc
import contextlib
import select
import time
import random
import socket
import struct
import threading
import subprocess
import warnings
import functools

from test import support
from test.support import (
    TESTFN, unlink, run_with_locale, check_warnings,
    check_no_resource_warning,
    cpython_only,
    )

# Skip these tests if there is no Unix socket support.
try:
    socket.socket(socket.AF_UNIX)
except OSError as e:
    if e.errno == errno.EAFNOSUPPORT:
        raise unittest.SkipTest("requires Unix sockets")
    raise

# Skip these tests if there is no IPv6 support.
try:
    socket.socket(socket.AF_INET6)
except OSError as e:
    if e.errno == errno.EAFNOSUPPORT:
        raise un
