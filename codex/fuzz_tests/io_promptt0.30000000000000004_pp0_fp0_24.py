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
import gc
import shutil
import contextlib
import pickle
import subprocess
import stat
import time
import socket
import select
import threading
import traceback
import warnings
from test import support
from test.support import TESTFN, unlink, run_with_locale, check_warnings
from test.support.script_helper import assert_python_ok

try:
    import resource
except ImportError:
    resource = None

try:
    import fcntl
except ImportError:
    fcntl = None

try:
    import msvcrt
except ImportError:
    msvcrt = None

try:
    import termios
except ImportError:
    termios = None

try:
    import array
except ImportError:
    array = None

try:
    import mmap
except ImportError:
    mmap = None

try:
    import _testcapi
except
