import weakref
# Test weakref.ref class.

import gc
import pickle
import sys
import types
import unittest

# To avoid the issues of having to deal with thread-local objects and
# thread-local storage, this module can be run in a single thread using
# the -single command-line option.  This is what the regrtest.py script
# does by default.  When the -single option is not used, each thread
# runs its own copy of the test code.  The main thread creates a threading.Barrier
# instance, whose wait() method is used to start each new thread.  When
# the thread is done executing its tests, it puts the result in a global
# list of results, releases the barrier and terminates.

single_thread = False

class TestRef(unittest.TestCase):
    def setUp(self):
        self.callback_args = []
        self.callback_result = None
        self.callback_exception = None
        self.callback_exc_info = None
        self.callback_called = 0

