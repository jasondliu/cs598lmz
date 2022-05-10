import mmap
import os
import sys
import tarfile
import tempfile
import time
import unittest

import setup

sys.path.insert(0, setup.src_dir)

from perfrunner.helpers.cbmonitor import with_stats
from perfrunner.helpers.misc import log_phase, pretty_dict


class PerfHelperTest(unittest.TestCase):

    def test_with_stats(self):
        @with_stats
        def my_function(a, b=None, c=None):
            return a + b + c

        self.assertEqual(my_function(1, 2, 3), 6)


class MiscHelperTest(unittest.TestCase):

    def test_pretty_dict(self):
        d = {'a': 'b', 'c': {'d': 'e', 'f': 'g'}, 'h': 'i'}
        self.assertEqual(pretty_dict(d),
                         "{'a': 'b',\n 'c': {'d': 'e', 'f': 'g'},\n
