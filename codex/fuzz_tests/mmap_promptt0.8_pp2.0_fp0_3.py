import mmap
# Test mmap.mmap(-1, 131072)
assert_raises(ValueError, mmap.mmap, -1, 131072)

# Test mmap.mmap(0, -1)
assert_raises(ValueError, mmap.mmap, 0, -1)

import os
import sys

def test_memmap_shapes():
    fp = open(TESTFN, 'wb')
    fp.write(b'1' * 1024)
    fp.close()
    m = mmap.mmap(fp.fileno(), 1024)
    fp = open(TESTFN, 'rb')
    a = np.memmap(fp, dtype=np.uint8)
    assert_equal(a.shape, (1024,))
    assert_equal(m[1:10], a[1:10])

    # test that a memmap can be mmap'ed
    m = mmap.mmap(fp.fileno(), 1024)
    fp = open(TESTFN, 'rb')
    a = np.memmap(fp,
