import mmap
# Test mmap.mmap

# open an existing file for reading
fd = os.open('/etc/hosts', os.O_RDONLY)

# create a new mmap starting at offset 0, the entire file size
# so we can read it.
m = mmap.mmap(fd, 0, access=mmap.ACCESS_READ)

# read content via standard file methods
