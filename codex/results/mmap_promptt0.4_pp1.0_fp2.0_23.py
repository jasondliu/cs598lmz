import mmap
# Test mmap.mmap()
#
# This test does not apply to Unix.
#
# The following test is only meaningful on Windows.
#
# The test is skipped if the system does not support mmap.
#
# mmap.mmap(fd, length[, access[, offset]])
#
# Create a new memory map using the file specified by the file handle fd,
# with an optional offset and length.  If length is omitted, the maximum
# length of the map is the current size of the file when mmap is called.
#
# The access argument specifies the access to the data.  The default value
# of access is mmap.ACCESS_WRITE.
#
# If offset is specified, it must be a multiple of the page size.
#
# The file handle fd must be open for mmap to succeed.
#
# The mmap object has these methods:
#
# close()
# Flush and close the memory map.  Changes to the memory mapped file may
# not appear in the file until close() is called.
#
# find(string[, start[, end]])
#
