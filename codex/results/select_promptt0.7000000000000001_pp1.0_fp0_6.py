import select
# Test select.select with a pipe.
import os
import unittest
import subprocess
import sys

def _create_and_close_fifo(name):
    # Calculate the location of the FIFO.
    start = os.path.abspath(os.curdir)
    try:
        fn = os.path.join(start, name)
        os.mkfifo(fn)
    except OSError as e:
        # Some platforms may not support FIFOs.
        if name == 'fifo' and e.errno == errno.ENOSYS:
            raise unittest.SkipTest('platform does not support fifo')
        raise
    else:
        # We don't need to keep the FIFO open, so close it before returning.
        f = os.open(fn, os.O_RDONLY)
        os.close(f)
        return fn


class SelectTestCase(unittest.TestCase):

    def setUp(self):
        self.path = _create_and_close_fifo('fifo')
       
