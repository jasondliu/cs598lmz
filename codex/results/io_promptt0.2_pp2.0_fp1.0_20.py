import io
# Test io.RawIOBase

import _io
import unittest
import weakref
import os
import sys
import io
import errno
import tempfile
import abc
import functools
import contextlib
import warnings
import pickle
import gc
import struct
import shutil
import stat
import subprocess
import threading
import time
import locale
import collections
import array

from test import support
from test.support import import_fresh_module

# Base test class for all IOBase tests

class BaseTestIO(metaclass=abc.ABCMeta):

    def setUp(self):
        self.thetype = self.io.IOBase
        self.rawio = self.io.RawIOBase
        self.iobase = self.io.IOBase
        self.bytesio = self.io.BytesIO
        self.stringio = self.io.StringIO
        self.tempfile = tempfile.TemporaryFile
        self.open = self.io.open
        self.filename = support.TESTFN
        self.f = None

    def tearDown(self):
