import select
# Test select.select(fd_list, [], []) with a read only file descriptor
import socket
import sys
import unittest
from unittest import mock
import weakref
from pprint import pprint as pp

from test.support import (
    import_fresh_module, run_unittest, socket_helper, verbose,
    TESTFN, unlink, captured_output, findfile, run_with_locale, cpython_only,
    check_warnings, BigaddrInUseWarning, socket_gaierror, bind_port
    )
from test.test_asyncio.test_base_events import Executor
from test.test_asyncio import utils as test_utils

try:
    import threading
except ImportError:
    threading = None


class TestSelect(unittest.TestCase):

    def test_error_conditions(self):
        self.assertRaises(ValueError, select.select, (), (), ())

        self.assertRaises(ValueError, select.select, (), (), (), -1.0)
        self.assertRaises
