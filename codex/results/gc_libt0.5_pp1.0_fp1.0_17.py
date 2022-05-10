import gc, weakref
import sys
import time
import unittest

from test import support
from test.support import import_module

# Skip this test if the _testcapi module isn't available.
_testcapi = import_module('_testcapi')

# Skip this test if the _testbuffer module isn't available.
_testbuffer = import_module('_testbuffer')

# Skip this test if the _testinternalcapi module isn't available.
_testinternalcapi = import_module('_testinternalcapi')

# Skip this test if the _testimportmultiple module isn't available.
_testimportmultiple = import_module('_testimportmultiple')

# Skip this test if the _testmultiphase module isn't available.
_testmultiphase = import_module('_testmultiphase')

# Skip this test if the _testcapimodule module isn't available.
_testcapimodule = import_module('_testcapimodule')

# Skip this test if the _testimportmultiple module isn't available.
_testimportmultiple = import_module('_
