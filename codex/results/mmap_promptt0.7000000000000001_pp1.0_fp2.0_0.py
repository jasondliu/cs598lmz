import mmap
# Test mmap.mmap(fileno, length[, tagname[, access[, offset]]])
# This method returns an object of mmap.mmap.
#
# fileno is a required integer or long value that specifies the file descriptor.
#
# length is a required integer or long value that specifies the number of bytes to map.
#
# tagname is an optional string or buffer value. If this argument is specified, the system will use it as the tagname in the shared memory region.
#
# access is an optional integer value that specifies the access to the memory. The default value is mmap.ACCESS_WRITE.
#
# offset is an optional integer or long value that specifies the byte offset for the start of the mapping.
#
# mmap.mmap(fileno, length)
#
# where fileno is a file descriptor
#
# length is the length of the memory to map.
#
# This mmap.mmap method returns an object of type mmap.mmap.
#
# Here is the example.
#
f = open('lorem.txt', 'r')
m = mmap.mmap
