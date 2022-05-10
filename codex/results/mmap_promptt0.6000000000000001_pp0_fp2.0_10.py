import mmap
# Test mmap.mmap()
#
# This test tries to exercise mmap module bug #662658:
# http://bugs.python.org/issue662658
#
# It also exercises mmap.read() and mmap.write() for offsets
# that are not multiples of mmap.ALLOCATIONGRANULARITY.
#
# It is known to expose the following bugs:
#
#   * mmap.read_byte() raises an exception on some platforms
#     when the offset is not a multiple of mmap.ALLOCATIONGRANULARITY.
#     (http://bugs.python.org/issue662658)
#
#   * mmap.write() writes extra bytes beyond the end of the mapped
#     region on some platforms when the offset is not a multiple
#     of mmap.ALLOCATIONGRANULARITY.  (http://bugs.python.org/issue662658)
#
#   * mmap.mmap() sometimes raises an exception when the length
#     is not a multiple of mmap.ALLOCATIONGRANULARITY.
#     (http://bugs.python.
