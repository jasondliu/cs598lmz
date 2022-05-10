import mmap
# Test mmap.mmap(...)
#
# Open a file for memory-mapping.
#
# by default the file is closed when mmap is destroyed
#
# If a file is opened in write-mode, changes made to the mmap object
# will be written to disk once the object is destroyed.
#
# If a file is opened in copy-on-write mode, changes made to the
# mmap object will be written to the copy-on-write (Anonymous) file.
# The copy-on-write file is allocated on the first write,
# and its contents are copied to the original file on close.
#
# If a file is opened in read-only mode, changes made to the mmap
# object will raise a TypeError exception.
#
# If a file is opened in asynchronous mode, changes made to the mmap
# object will return immediately.

# If you wish to access the data attribute of an mmap object,
# you must first ensure that the mmap object is resized to cover the
# area of the file you wish to access. This can be done using the resize()
# method.

# To check if
