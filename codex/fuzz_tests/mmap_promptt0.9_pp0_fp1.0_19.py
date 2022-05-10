import mmap
# Test mmap.mmap(-1,length,tagname="") for the ability to create a zero-length file
import sys

# bpo-34275: mmap might require 4k alignment.
#
# On Linux, if the underlying mmap(2) call fails with EINVAL, we assume
# that block device IO is not supported.  This means we have to
# increase the size of the buffer and try to mmap again.
#
# An alternative would be to always use os.SEEK_DATA, but that would cause
# a performance regression on Linux systems that support native block parallelism.
#
# On Windows, mmap is not able to be used to create a zero-byte file and
# work around this by mandating a minimum length that is >= 4k.
# See https://docs.python.org/3/library/mmap.html#mmap.mmap for more details.
def mmap_find_io_alignment(limit):
    alignments = {-1: 4096}
    for alignment in alignments:
        m = mmap.mmap(-1, alignment, tagname=b"")
       
