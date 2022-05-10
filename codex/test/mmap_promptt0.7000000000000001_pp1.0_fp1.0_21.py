import mmap
# Test mmap.mmap
mmap.mmap.__doc__

##rtype: mmap.mmap
##return: A mmap object.

## The mmap module defines the following exception:

## exception mmap.error
## This exception is raised on any error.

## The mmap module defines the following functions:

##mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
##fileno: 	an int, the file descriptor for the file to be mapped.
##length: 	an int, the number of bytes to map.
##flags: 	one of mmap.MAP_PRIVATE, mmap.MAP_SHARED, mmap.MAP_ANONYMOUS, optional.
##prot: 	one of mmap.PROT_READ, mmap.PROT_WRITE, mmap.PROT_EXEC, mmap.PROT_NONE, optional.
##access: 	mmap.ACCESS_COPY, mmap.ACCESS_READ, mmap.ACCESS_WRITE, optional.

