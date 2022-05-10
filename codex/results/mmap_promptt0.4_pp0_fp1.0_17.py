import mmap
# Test mmap.mmap()
#
# The mmap module supports the creation of memory-mapped files for all platforms.
#
# The mmap() function creates a new mmap object. The size argument specifies the
# initial size of the file mapping. The optional flags argument specifies how the
# file should be opened. The optional prot argument specifies the access permissions
# for the memory segment.
#
# The mmap() function returns a mmap object, which represents the mapped file.
#
# The mmap object supports the following methods:
#
# mmap.close()
# mmap.find(sub[, start[, end]])
# mmap.flush([offset[, size]])
# mmap.move(dest[, src, count])
# mmap.read(n)
# mmap.read_byte()
# mmap.readline()
# mmap.readlines()
# mmap.resize(new_size)
# mmap.rfind(sub[, start[, end]])
# mmap.seek(offset[, whence])
# mmap.size()
# mmap.tell
