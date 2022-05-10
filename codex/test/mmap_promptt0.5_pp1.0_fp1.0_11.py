import mmap
# Test mmap.mmap.read_byte() method
#

from mmap import *
from os import *
from os.path import *
import unittest

class MmapTests(unittest.TestCase):

    def setUp(self):
        fd = os.open(TESTFN, O_CREAT|O_RDWR)
        os.write(fd, '\0'*1024)
        os.close(fd)
        self.m = mmap(fd, 1024)

    def tearDown(self):
        self.m.close()
        os.unlink(TESTFN)

    def test_read_byte(self):
        self.assertEqual(self.m.read_byte(), '\0')
        self.assertEqual(self.m.read_byte(1), '\0')
        self.assertEqual(self.m.read_byte(2), '\0')
        self.assertRaises(ValueError, self.m.read_byte, 0)
