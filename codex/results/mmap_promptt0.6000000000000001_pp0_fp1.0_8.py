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

tests = [
    # This test maps the whole file read-only.  This should always
    # work.  It is the first test because it is the most likely to
    # fail.
    (None, None, mmap.ACCESS_READ, "Hello, world\n"),

    # This test maps the whole file read-write.  This should always
    # work.  It is the second test because it is the most likely to
    # fail.
    (None, None, mmap.ACCESS_WRITE, "Hello, world\n"),

    # This test maps the whole file read-execute.  This is likely to
