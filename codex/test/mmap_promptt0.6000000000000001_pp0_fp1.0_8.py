import mmap
# Test mmap.mmap()

#
# Test mmap.mmap()
#

# This is a list of tests to perform on mmap objects.  Each test is
# a tuple containing:
#  - The offset to map at (can be None to mean the current offset)
#  - The size of the mapping (can be None to mean the whole file)
#  - The access flags (see the docs for mmap.mmap())
#  - The expected result of the test

