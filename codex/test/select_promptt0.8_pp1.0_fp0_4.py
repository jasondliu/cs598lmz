import select
# Test select.select (5.5.2) with pipes for the read file descriptors,
# and the writing file descriptors and check that the reading file
# descriptors match the writing file descriptors.

from test.test_support import run_unittest, TESTFN, unlink

# The pipe() call returns a pair of file descriptors, r and w, which
# refer to the same pipe, as created by the pipe(2) system call.
r, w = os.pipe()

# Set up buffers.
read_buffer = ' ' * 1024
write_buffer = '-' * 1024

# Create a temporary file and write to it.
fp = open(TESTFN, 'wb')
fp.write(write_buffer)
fp.close()

# Open the temporary file and read from it.
fp = open(TESTFN, 'rb')

# Set up read and write lists.
read_list = [fp.fileno(), r]
write_list = [fp.fileno(), w]

# Test select.select function.  Select the reading file descriptors.
read_ready, write
