import mmap
# Test mmap.mmap.readline()
#
# $Id: test_readline.py,v 1.3 2004/08/11 16:15:36 gward Exp $

import os
import unittest
import mmap
from test.test_support import run_unittest, TESTFN, unlink


class ReadlineTestCase(unittest.TestCase):
    def setUp(self):
        fp = open(TESTFN, 'w+')
        fp.write('1+1\n2+2\n3+3\n')
        fp.close()

    def tearDown(self):
        unlink(TESTFN)

    def test_readline(self):
        fp = open(TESTFN, 'r+')
        m = mmap.mmap(fp.fileno(), 0)
        self.assertEqual(m.readline(), '1+1\n')
        self.assertEqual(m.readline(10), '2+2\n')
