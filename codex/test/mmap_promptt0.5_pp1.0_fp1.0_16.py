import mmap
# Test mmap.mmap(0, 1, access=mmap.ACCESS_WRITE)
#
# See also:
#   http://bugs.python.org/issue4766
#   http://bugs.python.org/issue14196
#   http://bugs.python.org/issue14197
#
# This test is meant to be run with a debug build of Python.
# It will crash if the bug is present.


def test_mmap_write_access_zero_length():
    m = mmap.mmap(0, 1, access=mmap.ACCESS_WRITE)
    m.close()


def test_mmap_write_access_zero_length_with_offset():
    m = mmap.mmap(0, 1, access=mmap.ACCESS_WRITE)
    m.close()


