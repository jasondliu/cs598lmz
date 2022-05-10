import mmap
# Test mmap.mmap as an alternative to numpy.memmap
#
# Author: Pearu Peterson <pearu.peterson@gmail.com>
# Created: April 2008
import os
import numpy
from numpy.testing import assert_equal, assert_, assert_almost_equal, assert_array_equal, TestCase

class TestMmap(TestCase):

    def setUp(self):
        self.name = 'tmp_mmap1.bin'
        self.shape = (2,3)
        self.dtype = 'd'

    def tearDown(self):
        try:
            os.unlink(self.name)
        except:
            pass

    def test_create(self):
        fp = open(self.name,'wb')
        fp.close()

    def test_mmap(self):
        a = numpy.zeros(self.shape, dtype=self.dtype)
        fp = open(self.name,'wb')
        a.tofile(fp)
        fp.close()

        fp = open(self.name,'
