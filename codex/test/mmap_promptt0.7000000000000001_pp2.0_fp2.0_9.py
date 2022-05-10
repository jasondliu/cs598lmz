import mmap
# Test mmap.mmap() and mmap.resize() for the case where we expand the
# mmap beyond the end of the file, and use PROT_WRITE.
#
# We have to use PROT_WRITE because if we use PROT_READ, then if we
# expand the mapping beyond the end of the file, the kernel has to fill
# in zeroes, which means we can't tell if it worked.
#
# mmap.mmap() takes an offset argument, so you can mmap a file starting
# at a nonzero offset, but there is no corresponding offset argument to
# mmap.resize(); we always resize the mapping starting at zero.  So to
# test this correctly, we need to mmap the file starting at a nonzero
# offset.
#
# If mmap.resize() is buggy, then we may get a SIGBUS from the mmap
# system call, or else the mmap call will appear to succeed, but we
# won't be able to write to the whole expanded region.
import os
import mmap
import tempfile
import unittest
from test import support
import sys
_4
