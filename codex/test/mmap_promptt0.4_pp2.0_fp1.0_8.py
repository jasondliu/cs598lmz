import mmap
# Test mmap.mmap()

# Create a new file in read/write mode
f = open("/tmp/mmaptest", "w+")

# Zero out the file to insure it's the right size
f.write("\x00" * mmap.PAGESIZE)

# Create the mmap instance with the following params:
# f.fileno() - pass in the file descriptor of the file
# mmap.PAGESIZE (could use 1024, 2048, 4096, 8192, etc)
# mmap.MAP_SHARED - changes are visible to other processes
# mmap.PROT_WRITE - pages may be written
# To modify the page you need to use mmap.PROT_WRITE
# Use mmap.PROT_READ for read-only maps
m = mmap.mmap(f.fileno(), mmap.PAGESIZE, mmap.MAP_SHARED, mmap.PROT_WRITE)
