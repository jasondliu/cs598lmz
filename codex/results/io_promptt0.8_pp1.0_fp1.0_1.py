import io
# Test io.RawIOBase
import os
import struct
import sys
import test.support
import unittest
import warnings
from test.support.script_helper import assert_python_ok, assert_python_failure
from test.support.script_helper import run_python_until_end
try:
    from _testcapi import raise_exception
except ImportError:
    raise_exception = None
try:
    import _thread
    _thread.start_new_thread
except ImportError:
    _thread = None
try:
    import _multiprocessing
except ImportError:
    _multiprocessing = None
try:
    import threading
except ImportError:
    threading = _thread
bytes_exception = (TypeError, ValueError)
else:
    bytes_exception = ()
b = bytes
memoryview_is_buffer = (memoryview is buffer)
try:
    compile(b('def f():\n raise BaseException\n'), '<stdin>', 'exec')
    can_compile_exc = 1
except TypeError:
   
