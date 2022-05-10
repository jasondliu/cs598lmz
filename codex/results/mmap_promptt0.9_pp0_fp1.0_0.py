import mmap
# Test mmap.mmap object by writing some data to it and then read that data from
# it.
# The mmap module defines the following functions:

# | mmap.mmap(fileno, length[, tagname[, access[, offset]]])
# | Create a new memory-mapped file.
# | The tagname, access and offset arguments are as described in the Unix manual
# | page. For example, specifying access=mmap.ACCESS_WRITE means that the
# | application intends to modify  the data. ACCESS_COPY makes a private copy of
# | the data, so modifications to the mmap object will not be written through to
# | the original object.
# | NOTE: If you intend to open a preexisting file to create a memory-mapped
# | file, use os.open() to open the file, and then pass the resulting file
# | descriptor value to fileno.
# | This function operates on UNIX systems, and on Windows. For Windows NT, the
# | tagname argument is ignored, but it must be None.
#
# | mmap.rfind(string[,
