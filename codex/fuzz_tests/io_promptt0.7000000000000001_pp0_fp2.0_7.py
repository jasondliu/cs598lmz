import io
# Test io.RawIOBase, io.BufferedIOBase and io.TextIOBase
import io
from io import RawIOBase, BufferedIOBase, TextIOBase
import abc
import unittest
import weakref
import tempfile
import contextlib
import sys
import os
import errno
import struct
import pickle
import shutil
import gc
from test import support
from test.support.script_helper import assert_python_ok
import subprocess
import warnings
from functools import partial

try:
    import threading
except ImportError:
    threading = None

# Base test class for testing IOBase subclasses.
#
# To test a new IOBase subclass, define a new class that inherits from
# this one.  You must define read_size to be the smallest readable unit,
# or None if the object is not readable, and write_size to be the smallest
# writable unit, or None if the object is not writable.  You must also
# define read_data and write_data, and optionally closed_data.
# If a file-like object is closed, you
