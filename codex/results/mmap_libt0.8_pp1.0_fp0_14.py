import mmap
import os
import py_compile
import sys
import tempfile
import threading
import unittest
import warnings
from test import support
from test.support.script_helper import assert_python_ok, assert_python_failure, make_script

# skip the test if _testcapi is not available
support.import_module('_testcapi')
from _testcapi import getargs_b

# Some tests require that sys.stdin, sys.stdout and sys.stderr are None
# (this was the case if it was never referenced before).  Since this test
# references those streams, in order to properly test the None case, we save
# the real streams.
__stdin__, __stdout__, __stderr__ = sys.stdin, sys.stdout, sys.stderr


MAGIC = b"<magic>"


class EmbeddingTests(unittest.TestCase):

    """Tests of the functions in Python/pythonrun.c (roughly)"""

    def setUp(self):
        self.sys_arg
