import io
# Test io.RawIOBase
import io
import os
import sys
import unittest
import warnings
import weakref
from test import support
from test.support import TESTFN, unlink, run_unittest
from test.support.script_helper import assert_python_ok
from test.support.script_helper import assert_python_failure
from test.support.script_helper import assert_python_exit_code
from test.support.script_helper import assert_python_warning
from test.support.script_helper import make_script
from test.support.script_helper import make_zip_script
from test.support.script_helper import make_pkg
from test.support.script_helper import make_zip_pkg
from test.support.script_helper import make_zip_pkg_with_bad_module
from test.support.script_helper import make_zip_pkg_with_init
from test.support.script_helper import make_zip_pkg_with_bad_init
from test.support.script_helper import make_zip_pkg_with_init_
