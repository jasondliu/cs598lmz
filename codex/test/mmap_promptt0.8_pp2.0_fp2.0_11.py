import mmap
# Test mmap.mmap() with various forms of offset.
#
# Note that this test uses Windows mmap() semantics, not Posix.
# Of particular note, Windows allows mmap()ing regions beyond the size of the
# file, which is disallowed by Posix.  This makes the test much simpler when
# examining negative offsets.

import os, sys
from test.support import TESTFN, unlink


with open(TESTFN, 'wb') as fobj:
    fobj.write(b'a' * 10)


def check_mapping(m, offset, size, access=mmap.ACCESS_WRITE):
    assert m.tell() == 0, 'initial position'
    m.seek(offset)
    loc = m.tell()
    assert loc == offset
    m[loc] = b'B'
    m.flush()
    with open(TESTFN, 'rb') as fobj:
        fobj.seek(offset)
        value = fobj.read(1)
    assert value == b'B'

    # Verify that reading returns the correct number of bytes.

   
