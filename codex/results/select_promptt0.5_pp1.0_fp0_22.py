import select
# Test select.select()
#
#

import sys

if sys.platform == 'win32':
    import socket
    from socket import AF_INET, SOCK_STREAM
    from socket import error as sock_error
else:
    from select import error as select_error

from test.support import (
    run_unittest,
    import_module,
    findfile,
    get_attribute,
    unlink,
    TESTFN,
    )

import unittest
from unittest import mock

import_module('threading')
# Skip test if semaphore implementation is broken.
import_module('_thread')
# Skip test if thread implementation is broken.
import_module('_threading_local')
# Skip test if threading local implementation is broken.
import_module('time')
# Skip test if time.sleep() implementation is broken.

class SelectTestCase(unittest.TestCase):

    def setUp(self):
        self.save_warnings_state()
        warnings.filterwarnings('ignore', '', DeprecationWarning,
                
