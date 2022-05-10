import io
# Test io.RawIOBase to avoid circular import
if sys.version_info[:2] == (3, 4):  # pragma: no branch
    if sys.version_info[:3] == (3, 4, 0):
        # This is a regression in 3.4.0
        raise unittest.SkipTest('circular import regression in 3.4.0')
    else:
        raise unittest.SkipTest('circular import problem in 3.4')

import socket
import sys
import threading
import time
import unittest

import gevent
from gevent import event, socket, threading, local, thread

from greentest import TestCase, main, get_error_handler, sysinfo
from greentest.test__threading import TestEvent as _TestEvent
from greentest.util import wrap_errors, get_free_port


class TestCaseNoStandardError(TestCase):
    # TestCase logs errors to stderr by default, but we don't
    # want to see them in the test results

    def tearDown(self):
        self.switch_expected_
