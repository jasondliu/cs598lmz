import mmap
# Test mmap.mmap()
# fd     Must be an open file descriptor (a positive integer as returned by a file object’s fileno() method). It has to be opened in read-write mode.
# length Specifies the length of the mapping (which must be greater than zero). The default is the current size of the file.
# flags  Optional flags for the mapping (see below). The default value is zero (no flags).
# prot   The desired memory protection for the mapping (see below). The default value is PROT_WRITE.
# access May specify whether you wish to create a private or shared mapping. The default value is ACCESS_DEFAULT.

# The following symbolic constants are used to construct values for the prot argument to mmap(). The PROT_WRITE constant stands for write permission:
PROT_READ  = internal['PROT_READ']  # Pages may be read.
PROT_WRITE = internal['PROT_WRITE'] # Pages may be written.
PROT_EXEC  = internal['PROT_EXEC']  # Pages may be executed.
PROT_NONE  = internal['PROT_NONE']  #
