import io
# Test io.RawIOBase

import unittest
import io
import os
import os.path
import sys
import tempfile
import weakref
import pickle
import gc
import random
import shutil
import errno
import stat
import contextlib

from test import test_support

# Skip tests if there is no implementation of io.RawIOBase.
if not hasattr(io, "RawIOBase"):
    raise unittest.SkipTest("RawIOBase not implemented")

# Skip tests if io.FileIO is not implemented.
if not hasattr(io, "FileIO"):
    raise unittest.SkipTest("FileIO not implemented")

# Skip tests if io.BufferedIOBase is not implemented.
if not hasattr(io, "BufferedIOBase"):
    raise unittest.SkipTest("BufferedIOBase not implemented")

# Skip tests if io.BufferedReader is not implemented.
if not hasattr(io, "BufferedReader"):
    raise unittest.SkipTest("BufferedReader not implemented")

# Skip tests if io.BufferedWriter
