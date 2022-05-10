import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import pickle
import contextlib
import random
import shutil
import subprocess
import threading
import time
import errno
import gc

from test import support
from test.support import TESTFN, unlink, run_with_locale, import_module
from test.support.script_helper import assert_python_ok

# Skip tests if _io.FileIO is not available.
FileIO = import_module('_io').FileIO

# Skip tests if the _winapi module is not available.
winapi = import_module('_winapi')

# Skip tests if the _multiprocessing module is not available.
mp = import_module('_multiprocessing')

# Skip tests if the _posixsubprocess module is not available.
posixsubprocess = import_module('_posixsubprocess')

# Skip tests if the _testcapi module is not available.
_testcapi = import_module('_testcapi')

#
