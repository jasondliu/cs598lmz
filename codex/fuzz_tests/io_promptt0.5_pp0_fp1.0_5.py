import io
# Test io.RawIOBase

import unittest
import weakref
import os
import errno
import sys
import io
import _io
import _testcapi
import contextlib
import functools
import struct
import tempfile
import threading
import time
import subprocess
import pickle
import gc

from test import support

# A mixin for testing RawIOBase objects.
#
# To use, define a class C that inherits from RawIOMixin and unittest.TestCase,
# and define C.setUp().  C.setUp() should create an instance self.io of the
# object to be tested, and set self.filename to a filename that can be used to
# construct a second, independent object.
#
# If the object to be tested requires a filename to be given to the constructor
# (as opposed to an existing file object), define C.filename to be the
# filename, and C.setUp() can be empty.
#
# If the object to be tested does not require a filename, define C.setUp() to
# create the object, and set C.filename to None
