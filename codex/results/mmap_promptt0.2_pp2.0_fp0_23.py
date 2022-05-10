import mmap
# Test mmap.mmap()
#
# This test is designed to test the mmap.mmap() function.
#
# The test is designed to be run in a sub-process so that it can
# test the mmap.mmap() function without affecting the parent process.
#
# The test will create a file and then use mmap.mmap() to map the file
# into memory.  The test will then write to the file and verify that
# the data written is visible in the memory map.
#
# The test will then close the memory map and verify that the data
# written to the memory map is visible in the file.
#
# The test will then unlink the file and verify that the file is
# removed.
#
# The test will then create a file and use mmap.mmap() to map the file
# into memory.  The test will then write to the file and verify that
# the data written is visible in the memory map.
#
# The test will then close the file and verify that the data written
# to the memory map is visible in the file.
#
# The test will then unlink the file and
