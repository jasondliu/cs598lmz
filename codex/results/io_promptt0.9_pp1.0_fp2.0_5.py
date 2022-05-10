import io
# Test io.RawIOBase, a base class for raw binary I/O.

import io
import os
import pickle
from test import support

from test import test_io
from test.support import TESTFN, run_with_locale, _fake_rlock, check_warnings

from io import BufferedWriter, BufferedRandom, BufferedRWPair, DEFAULT_BUFFER_SIZE

from UserList import UserList

from math import hypot


class TestRawIOBase(test_io.BaseTestIO):

    def test_args(self):
        if support.verbose:
            print('Testing argument passing...')
        for B in [io.RawIOBase, io.FileIO]:
            # test that positional arguments are accepted
            f = B(*self._get_args(support.TESTFN, 'w+'))
            # test that keyword arguments are accepted
            f = B(**self._get_args(support.TESTFN, 'w+b'))
            f.close()
            unlink(support.TESTFN)
            # test that keyword arguments can hide the file name
