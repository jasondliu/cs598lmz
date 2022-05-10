import io
# Test io.RawIOBase

import io
import unittest
import weakref
import sys
import os
import errno
import _io
import _testcapi
import tempfile
import contextlib
import gc
import subprocess
import select
import time
import shutil
import stat
from test import support
from test.support import bigmemtest, TESTFN, unlink, run_with_locale, \
    import_module, cpython_only, check_warnings
from test.support.script_helper import assert_python_ok
from test.support.os_helper import TESTFN_UNENCODABLE

# Base class for testing io.RawIOBase.
# The tests are constructed from the read(), readinto() and write()
# methods.
class BaseRawIO(io.RawIOBase):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.read_stack = []
        self.write_stack = []
        self.readinto_stack = []

    def read(self, n=-
