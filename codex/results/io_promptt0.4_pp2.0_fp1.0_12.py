import io
# Test io.RawIOBase

import _io
import unittest
import weakref
import os
import sys
import io
import errno
import pickle
import shutil
import tempfile
import contextlib
import itertools
import functools
import collections
import collections.abc
import abc
import operator
import threading
import time
import warnings
import random
import subprocess

from test import support
from test.support import (
    TESTFN, unlink, import_module, run_unittest, cpython_only, check_warnings,
    check_impl_detail, bigmemtest, _2G, _4G, _4Gplus1, _test_generic_path
)
from test.support.script_helper import assert_python_ok

try:
    import thread
except ImportError:
    thread = None

# This is used for testing the "buffering" argument of open().
DEFAULT_BUFFER_SIZE = io.DEFAULT_BUFFER_SIZE

# This is used for testing the "encoding" and "errors" arguments of open().
FS_ENCOD
