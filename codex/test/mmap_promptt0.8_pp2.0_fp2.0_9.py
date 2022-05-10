import mmap
# Test mmap.mmap

# Open a file for reading.  There's a short time window after the open
# when the file size is zero but the file exists.  Not sure if it is
# possible to slip in and map that.
fd = os.open("/tmp/xxx", os.O_RDONLY)
# Wait until the file is created
time.sleep(3)
m = mmap.mmap(fd, 0, mmap.MAP_SHARED, mmap.PROT_READ)

# This should read the first character of the file
