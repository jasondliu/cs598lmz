import mmap
# Test mmap.mmap()
#
# This test is intended to be run from the top level directory of the
# mmap distribution, as:
#
#   python Lib/test/test_mmap.py
#
# It is also run as part of the Python regression test suite.
#
# This test requires the Python test framework "pytest" to be installed.

import os
import sys
import unittest
import errno
import tempfile
import stat
import shutil
import io
import struct
import functools
import subprocess
import warnings
import contextlib
import platform
import pickle
import array
import mmap
import gc
import weakref
import re
import textwrap
import traceback
import random
from test import support

try:
    import _testcapi
except ImportError:
    _testcapi = None

try:
    import fcntl
except ImportError:
    fcntl = None

try:
    import mmap
except ImportError:
    mmap = None

try:
    import _winapi
except ImportError:
    _
