import mmap
# Test mmap.mmap with read-only permissions

# It's important to open the file in binary mode, otherwise the
# behaviour of the fileops on the mapped region are undefined.
