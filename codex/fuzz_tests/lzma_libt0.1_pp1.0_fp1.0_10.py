import lzma
lzma.LZMAError

import os
import sys
import time
import shutil
import subprocess
import tempfile
import unittest
import warnings

from test import support
from test.support import TESTFN, run_unittest, unlink, unload, import_module
from test.support.script_helper import assert_python_ok

# Skip test if the implementation is CPython and -OO was passed.
requires_docstrings = unittest.skipIf(
        sys.flags.optimize >= 2,
        "Docstrings are omitted with -OO and above")

# Skip test if the implementation is PyPy and -OO was passed.
requires_docstrings_py3k = unittest.skipIf(
        sys.flags.optimize >= 2 and sys.implementation.name == 'pypy',
        "Docstrings are omitted with -OO and above")

# Skip test if the implementation is CPython and -OO was passed.
requires_docstrings_cpython = unittest.skipIf(
        sys.flags.optimize >= 2 and sys.implementation.
