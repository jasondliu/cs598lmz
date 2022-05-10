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

