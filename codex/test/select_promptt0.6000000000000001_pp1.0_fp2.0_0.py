import select
# Test select.select for a file descriptor

import os
import sys
import time

from select import select

from test.support import run_unittest, TESTFN, unlink

class FileTestsBase(unittest.TestCase):
    def setUp(self):
        self.f = open(TESTFN, 'wb')

    def tearDown(self):
        self.f.close()
        unlink(TESTFN)

    def check_read_ready(self):
        fd = self.f.fileno()
        self.f.write(b'abc\n')
        self.f.flush()
        time.sleep(0.01)
        r, w, x = select.select([fd], [], [], 0.1)
        self.assertTrue(r)

    def check_write_ready(self):
        fd = self.f.fileno()
        self.f.write(b'abc\n')
        self.f.flush()
        time.sleep(0.01)
