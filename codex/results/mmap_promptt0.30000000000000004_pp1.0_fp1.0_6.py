import mmap
# Test mmap.mmap
#
# This is a simple test to see if mmap.mmap works.
#
# The test is to create a file with some data, then mmap the file and
# verify that the data is correct.
#
# This test is a little different than the other tests in this directory
# in that it actually creates a file on the file system.  This is done
# because the mmap module is used to map files, and there is no way to
# create a file without writing it to the file system.
#
# This test is also different in that it uses the mmap module directly,
# rather than using the os module to access the mmap functionality.
#
# The test is run using the following commands:
#
#   python mmap_test.py
#
# The test passes if the output looks like this:
#
#   mmap_test.py
#   test_mmap_1: PASS
#   test_mmap_2: PASS
#   test_mmap_3: PASS
#   test_mmap_4: PASS
#   test_mmap_5: PASS
