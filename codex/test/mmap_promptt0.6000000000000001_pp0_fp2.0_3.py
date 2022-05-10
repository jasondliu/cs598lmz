import mmap
# Test mmap.mmap function
#
# This function is used to map a file into memory.
#
# It has the following syntax:
#
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
#
# Here is the description of the parameters:
#
# fileno - This is the file descriptor returned by os.open().
# length - This is the length of the mapping (which must be less than the
# length of the file).
# flags - This is one of mmap.MAP_SHARED, mmap.MAP_PRIVATE, mmap.MAP_ANONYMOUS,
# mmap.MAP_ANON.
# prot - This is the page protection flag. It can be one of the following:
# mmap.PROT_EXEC, mmap.PROT_READ, mmap.PROT_WRITE, mmap.PROT_NONE. One can also
# use the bitwise OR operator to combine these values.
# access - This is either mmap.ACCESS_DEFAULT or mmap.ACCESS_COPY.

