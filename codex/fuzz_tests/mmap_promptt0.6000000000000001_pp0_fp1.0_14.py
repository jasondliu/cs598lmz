import mmap
# Test mmap.mmap()
import os
# Test os.stat()
import shutil
# Test shutil.rmtree()
import sys
# Test sys.platform
import tempfile
# Test tempfile.mkstemp()
import unittest
# Test unittest.TestCase

from pyodide import fs
# Test fs.open()

import pyodide._python as _python

# Test _python.set_sys_argv()
# Test _python.get_sys_argv()
# Test _python.get_sys_executable()
# Test _python.get_sys_path()
# Test _python.get_sys_stdin()
# Test _python.get_sys_stdout()
# Test _python.get_sys_stderr()
# Test _python.get_sys_version()
# Test _python.get_sys_version_info()

# In order to test the Python C API, we need to be able to load a dynamic
# library from Python. We do this by creating a small dynamic library which
# can be loaded from Python, which will in turn
