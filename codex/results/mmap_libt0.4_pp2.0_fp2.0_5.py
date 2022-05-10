import mmap
import os
import re
import sys
import threading
import time
import traceback
import types
import unittest

import six

from six.moves import xrange

from test import support

# Skip this test if the _multiprocessing module isn't available.
_multiprocessing = support.import_module('_multiprocessing')
# Skip this test if sem_open implementation is not correct.
support.requires('semaphore')

from test.fork_wait import ForkWait

#
#
#

TIMEOUT1, TIMEOUT2, TIMEOUT3 = 0.1, 0.2, 0.3

#
# Constants
#

SEMAPHORE_VALUE = 1234

#
#
#

class BaseTestCase(ForkWait):

    ALLOWED_TYPES = ('processes',)

    def manager_class(self):
        return _multiprocessing.managers.SyncManager

    def test_Manager(self):
        m = self.manager_class()
        self.assert
