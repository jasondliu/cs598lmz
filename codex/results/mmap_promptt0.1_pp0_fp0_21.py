import mmap
# Test mmap.mmap()
#
# This test is based on the test_mmap.py test module from the Python
# standard library.

import os
import sys
import unittest
import mmap
import struct
import array
import tempfile
import io
import contextlib
import warnings
import errno
import functools
import gc
import pickle
import shutil
import subprocess
import time
import test.support
import test.support.script_helper
import test.support.temp_cwd
import test.support.threading_helper
import test.support.warnings_helper
import test.support.os_helper
import test.support.cpython_only
import test.support.script_helper
import test.support.temp_cwd
import test.support.threading_helper
import test.support.warnings_helper
import test.support.os_helper
import test.support.cpython_only

# Skip tests if the _testcapi module isn't available.
test.support.import_module('_testcapi')

# Skip tests
