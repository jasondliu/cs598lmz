import io
# Test io.RawIOBase
import os
import socket
import sys
import tempfile
import weakref
import unittest
from test import support
from test.support import threading_helper, bigaddrspacetest
from test.support.script_helper import assert_python_ok
from test.support.threading_helper import reap_threads
from test.support.import_helper import import_module
try:
    import threading
except ImportError:
    threading = None
try:
    import _thread
except ImportError:
    _thread = None
try:
    import fcntl
except ImportError:
    fcntl = None
try:
    import _pyio
except ImportError:
    _pyio = None
try:
    import mmap
except ImportError:
    mmap = None
try:
    import _winapi
except ImportError:
    _winapi = None
try:
    import _multiprocessing
except ImportError:
    _multiprocessing = None
try:
    import _locale
except ImportError:
   
