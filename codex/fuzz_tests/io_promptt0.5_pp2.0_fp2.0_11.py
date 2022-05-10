import io
# Test io.RawIOBase.readinto()
import io
import _io
import unittest
import sys
import os
from io import UnsupportedOperation
import pickle
import select
import errno
import subprocess
import contextlib
import socket
import tempfile
import threading
import time
import array
import warnings
import random
import gc
import itertools
import shutil
import weakref
import re
import reprlib
import collections
from test import support
from test.support import os_helper
from test.support.script_helper import assert_python_ok
from test import mock_helpers
from test import lock_tests
import platform
import sysconfig
try:
    import thread
except ImportError:
    import _thread as thread
try:
    import _pyio as pyio
except ImportError:
    import pyio
try:
    import mmap
except ImportError:
    mmap = None
try:
    import resource
except ImportError:
    resource = None
try:
    import fcntl
except ImportError:
    fcntl = None
try:

