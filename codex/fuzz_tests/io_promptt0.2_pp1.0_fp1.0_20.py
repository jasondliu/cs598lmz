import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno
import pickle
import weakref
import gc
import random
import struct
import subprocess
import warnings
import contextlib
from test import support
from test.support import import_module
from test.support.script_helper import assert_python_ok
from test.support.os_helper import TESTFN, unlink, unlink_if_exists
from test.support.script_helper import assert_python_failure

# Base class for testing a raw I/O implementation.
#
# The setUp() method creates a raw I/O object for testing.  The object is
# accessible to the test methods as self.the_object.  The tearDown() method
# closes the object.
#
# Subclasses should override setUp() to create the object with a specific
# implementation.  setUp() should call the base class setUp() to ensure that
# the object is created.  Subclasses should also override tearDown() to
# close the object with the specific implementation.  tearDown() should
