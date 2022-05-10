import mmap
# Test mmap.mmap
#
# This is a test script for mmap.mmap objects.
#
# Note:
#
#    1. This test script assumes that mmap.PAGESIZE == 4096
#    2. This test script assumes that sizeof(long) == 4
#
# To run this test script, use the following command line:
#
#    python test_mmap.py
#
# The test script will print "Test passed." if the test passes.
# Otherwise, it will print "Test failed." and raise an exception.

# Test mmap.mmap.__new__
#
# This test creates a mmap.mmap object and checks that the object
# is created correctly.

# Create a mmap.mmap object.
m = mmap.mmap(-1, 4096)

# Check that the object is a mmap.mmap object.
if not isinstance(m, mmap.mmap):
    raise Exception("Test failed.")

# Check that the object is a read/write memory map.
if m.read_only:
    raise Exception("Test failed.")


