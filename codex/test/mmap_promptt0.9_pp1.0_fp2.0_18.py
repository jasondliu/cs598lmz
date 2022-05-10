import mmap
# Test mmap.mmap(fileno, ...).move(0, 0, offset)
import os
import random
import subprocess
import sys
import time
import unittest

import _multiprocessing
from test import test_support
from test.fork_wait import ForkWait
from test import multiwait

if _multiprocessing.HAVE_SEM_OPEN:
    from _multiprocessing import SemLock


def tobytes(obj):
    s = str(obj)
    if 'b' in s:
        s = s[s.index('b') + 1:]
    return eval(s, {'__builtins__':{}})


class BaseTestCase(unittest.TestCase):

    ALLOWED_TYPES = ('processes',)

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix='pymaptest_')
