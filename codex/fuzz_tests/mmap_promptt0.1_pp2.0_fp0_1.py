import mmap
# Test mmap.mmap()
#
# This test is based on the example in the mmap documentation.

import mmap
import os
import struct
import sys
import unittest

from test import support

# The size of the mmap'ed file.
size = 1024

# The number of times to repeat the test.
count = 10

# The number of times to repeat the test when using a file descriptor.
fd_count = 10

# The number of times to repeat the test when using a file descriptor
# and a size of 0.
fd_zero_count = 10

# The number of times to repeat the test when using a file descriptor
# and a size of 0 and access=ACCESS_READ.
fd_zero_read_count = 10

# The number of times to repeat the test when using a file descriptor
# and a size of 0 and access=ACCESS_WRITE.
fd_zero_write_count = 10

# The number of times to repeat the test when using a file descriptor
# and a size of 0 and access=ACCESS_COPY.
fd_zero_copy_count
