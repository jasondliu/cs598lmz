import mmap
# Test mmap.mmap.resize() on non-writable mappings
import os
import struct
import sys
import unittest

from test import support


PAGESIZE = os.sysconf('SC_PAGE_SIZE')
BUFSIZE = 3 * PAGESIZE

with support.temp_dir() as tmpdir:
    filename = os.path.join(tmpdir, 'mmap_largefile')
    with open(filename, 'wb') as f:
        f.write(b'\x00' * BUFSIZE)

    with open(filename, 'rb') as f:
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
            m.seek(2 * PAGESIZE)
            data = m.read(PAGESIZE)
            self.assertEqual(len(data), PAGESIZE)
            self.assertEqual(data, b'\x00' * PAGESIZE)
            self.assertRaises(ValueError, m.resize, 0)
            m.seek(0)
