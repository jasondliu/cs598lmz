import mmap
# Test mmap.mmap()
#
# This test is designed to test the mmap.mmap() function.
#
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
#
# fileno is the file descriptor of the file to be mapped.
# length is the length of the mapping.
# flags is the bitwise OR of mmap.MAP_PRIVATE, mmap.MAP_SHARED,
# mmap.MAP_ANONYMOUS, and mmap.MAP_ANON.
# prot is the bitwise OR of mmap.PROT_EXEC, mmap.PROT_READ, and
# mmap.PROT_WRITE.
# access is either mmap.ACCESS_DEFAULT or mmap.ACCESS_COPY.
# offset is the offset into the file.
#
# This test will test the following flags:
# mmap.MAP_PRIVATE
# mmap.MAP_SHARED
# mmap.MAP_ANONYMOUS
# mmap.MAP_ANON
# mmap.PROT
