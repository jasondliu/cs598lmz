import mmap
# Test mmap.mmap()
# Create a memory-map to an integer variable
# (Memory-mapped file objects behave like both bytearray and like file objects)
length = mmap.PAGESIZE
with open("data.dat", "w+b") as f:
    # zero-out the memory
    f.write(bytes(length))

f = open("data.dat", "r+b")
# memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)
# read/write to the mapped region as if it were a bytearray
m[0:16] = b"Hello"
m[0:5]
# close the map and file
m.close()
f.close()

