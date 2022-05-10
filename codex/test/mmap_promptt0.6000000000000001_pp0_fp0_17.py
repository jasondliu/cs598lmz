import mmap
# Test mmap.mmap(0, 1, access=mmap.ACCESS_READ)

import os
# Test os.O_RDONLY, os.O_WRONLY, and os.O_RDWR

from struct import pack
# Test pack('i', 0)

from sys import platform
# Test platform

from unittest import TestCase, main

from numpy import zeros
# Test zeros(10, dtype='i4')


class TestMmap(TestCase):
    def test_mmap_from_memory(self):
        # Check that we can create a small mmap that is just large
        # enough to hold the data we want to write.
        m = mmap.mmap(0, 16, access=mmap.ACCESS_WRITE)
        m.write(pack('i', 1))
        m.write(pack('i', 2))
        m.write(pack('i', 3))
        m.write(pack('i', 4))
        m.seek(0)
