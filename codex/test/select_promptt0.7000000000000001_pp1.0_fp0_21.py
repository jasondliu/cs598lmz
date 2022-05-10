import select
# Test select.select behavior on invalid file descriptors.
from test.support import run_unittest, reap_threads, import_module, find_unused_port, socket_helper

try:
    select = import_module('select')
except ImportError:
    raise unittest.SkipTest('the select module is not available')

# Base class for the tests.
