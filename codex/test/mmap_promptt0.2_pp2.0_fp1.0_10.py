import mmap
# Test mmap.mmap()
#
# This test is for mmap.mmap()
#
# The test is to verify that mmap.mmap() can be used to create a memory map
# to an entire file.
#
# The test will create a file of a specified size and then create a memory
# map to the entire file.  The test will then write to the memory map and
# verify that the data written is the same as the data read.
#
# The test will then close the memory map and reopen it and verify that the
# data written is the same as the data read.
#
# The test will then close the memory map and reopen it with the access
# set to mmap.ACCESS_READ and verify that the data written is the same as
# the data read.
#
# The test will then close the memory map and reopen it with the access
# set to mmap.ACCESS_WRITE and verify that the data written is the same as
# the data read.
#
# The test will then close the memory map and reopen it with the access
# set to mmap.ACCESS_COPY and verify that
