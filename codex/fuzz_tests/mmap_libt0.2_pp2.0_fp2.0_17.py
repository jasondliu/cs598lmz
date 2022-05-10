import mmap
import os
import re
import sys
import tempfile
import time
import traceback
import types
import unittest
import warnings

from test import support
from test.support import (
    TESTFN, unlink, unload, import_module, run_unittest,
    check_warnings, captured_output,
    cpython_only, requires_zlib, requires_bz2, requires_lzma,
    requires_gzip, requires_pyio, requires_py3k,
    bigmemtest, bigaddrspacetest,
    )

import gzip
import zlib
import bz2
import lzma

# The module to be tested
gzip = import_module('gzip')

# Helper for saving and restoring the contents of sys.path
path_save = None
def set_path_save():
    global path_save
    path_save = sys.path[:]
def restore_path():
    sys.path = path_save

# Helper for creating temporary files
def make_temp_file(content, dir=None):
