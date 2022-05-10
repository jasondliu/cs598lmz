import io
# Test io.RawIOBase.read()
import os
import sys
import random
import signal
import socket
import threading
import time
import traceback
# Abstract base class
try:
    import thread
except ImportError:
    import _thread as thread
try:
    import cPickle as pickle
except ImportError:
    import pickle

# Python 2 compat
if sys.version_info[0] == 2:
    import Queue as queue
    TimeoutError = socket.timeout
    try:
        from collections import OrderedDict
    except ImportError:
        from ordereddict import OrderedDict
else:
    import queue
    import collections.abc as abc
    TimeoutError = TimeoutError

address_size = struct.calcsize('P')

# For testing
import errno
import platform
import unittest
import warnings

# Windows support
TEST_FILENAME = "test"
WINDOWS = (platform.system() == "Windows")
if WINDOWS:
    import msvcrt
    import _overlapped
    from _multiprocessing
