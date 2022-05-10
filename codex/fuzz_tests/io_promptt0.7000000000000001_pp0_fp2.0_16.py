import io
# Test io.RawIOBase

import _io
try:
    from _io import open
except ImportError:
    pass
import _testcapi
import contextlib
import errno
import os
import random
import shutil
import stat
import sys
import tempfile
import threading
import time
import unittest
from test import support
from test.support import import_module
# Skip tests if _thread or _winapi are not available.
threading = import_module('_thread')
winapi = import_module('_winapi')
try:
    import fcntl
except ImportError:
    fcntl = None
if hasattr(os, 'dup'):
    def _dup(fd):
        return os.dup(fd)
else:
    def _dup(fd):
        raise NotImplementedError()
if hasattr(os, 'dup2'):
    def _dup2(a, b):
        return os.dup2(a, b)
else:
    def _dup2(a, b):
        raise NotImple
