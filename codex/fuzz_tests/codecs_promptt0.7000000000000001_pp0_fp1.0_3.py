import codecs
# Test codecs.register_error()
from codecs import register_error

# Test Py_UNICODE_WIDE
from sys import maxunicode as maxunicode

from sys import intern as intern

from test import test_support
from test.test_support import run_unittest, import_module
from test.test_support import captured_stdout, captured_stderr

from test.test_support import check_impl_detail
from test.test_support import unicode_output, unicode_input
from test.test_support import unlink

from test.script_helper import make_script

from test.script_helper import assert_python_ok
from test.script_helper import assert_python_failure
from test.script_helper import assert_python_failure_and_traceback
from test.script_helper import is_jython

import unittest
from UserList import UserList
from UserString import UserString

def dummy_encode(input, errors='strict'):
    return (input.encode(), len(input))

# Register an error
