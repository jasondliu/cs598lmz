import mmap
# Test mmap.mmap()

# Mmap from file
f = open('lorem.txt', 'r')
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
toPrint = m.readline()
