import mmap
# Test mmap.mmap()
m = mmap.mmap(fd, 0)
m # should print <mmap closed file 'parcels.0.0.nc', 2560000 bytes>
