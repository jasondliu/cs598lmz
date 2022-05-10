import codecs
# Test codecs.register_error()
import os
import re
import sys
import time
import unittest
from test import support
from test.support import TESTFN, unlink, run_unittest, import_module
from test.script_helper import assert_python_ok, assert_python_failure

# Skip test if _testcapi isn't available.
testcapi = import_module('_testcapi')

# Skip test if _testbuffer isn't available.
testbuffer = import_module('_testbuffer')

# Skip test if _testbuffer doesn't have the buffer_info() function.
testbuffer.buffer_info

# Skip test if _testimportmultiple is not available.
testimportmultiple = import_module('_testimportmultiple')

# Skip test if _testinternalcapi is not available.
testinternalcapi = import_module('_testinternalcapi')

# Skip test if _testmultiphase is not available.
testmultiphase = import_module('_testmultiphase')

# Skip test if _testcapimodule is not available.
testcapimod
