import mmap
# Test mmap.mmap()
#
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
#
# fileno:
#   An integer file descriptor of the file to be mapped.
#   If the file is opened in text mode, you must open it in binary mode
#   (usually by appending 'b' to the mode argument).
#
# length:
#   The number of bytes to map, or mmap.ALLOCATIONGRANULARITY to map the whole file.
#
# flags:
#   The flags argument specifies the nature of the mapping.
#   It is a bitwise OR of one or more of the following constants:
#   mmap.ACCESS_READ, mmap.ACCESS_WRITE, mmap.ACCESS_COPY
#
# prot:
#   The prot argument describes the desired memory protection of the mapping
#   (and must not conflict with the open flags).
#   It is a bitwise OR of one or more of the following constants:
#   mmap.PROT_EXEC, mmap.PROT_READ
