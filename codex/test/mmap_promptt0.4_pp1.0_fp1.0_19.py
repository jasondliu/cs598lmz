import mmap
# Test mmap.mmap()
#
# This test is used to test the mmap.mmap() function.
#
# mmap.mmap(fileno, length[, tagname[, access[, offset]]])
#
# fileno: A file descriptor that refers to a file opened for update.
# length: The size of the mapping (which must be less than or equal to the
#         file size).
# tagname: An optional file name used to identify the mapping in debugging
#          output or logs.
# access: The access policy. Can be mmap.ACCESS_READ, mmap.ACCESS_WRITE, or
#         mmap.ACCESS_COPY. Default value: mmap.ACCESS_WRITE.
# offset: Where in the file to start the mapping. Must be a multiple of the
#         system's page size. Default value: 0.
#
# Returns a memory-mapped object.
#
# mmap.mmap() raises an exception if the creation fails.
#
# mmap.mmap() returns a mmap object on success.
#
# mmap.mmap
