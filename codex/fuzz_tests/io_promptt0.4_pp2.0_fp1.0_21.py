import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import threading
import weakref
import pickle
import subprocess
import errno
import functools
import collections
import contextlib
import struct
import time
import textwrap
import socket
import select
import gc
import atexit

from test import support
from test.support.script_helper import assert_python_ok
from test.support import os_helper
from test.support import import_helper

# XXX This test module is a mess.  It needs to be cleaned up.

# Base class for testing a given IOBase implementation.
# This is *not* meant to be a public interface!
class IOBaseTests(object):

    # Subclasses can override.
    os_supports_direct_reads = True

    def test_attributes(self):
        rawio = self.RawIOClass(self.FileIO(support.TESTFN, "wb"))
        self.assertIsInstance(rawio, io.RawIOBase)
        self.assertIsInstance(raw
