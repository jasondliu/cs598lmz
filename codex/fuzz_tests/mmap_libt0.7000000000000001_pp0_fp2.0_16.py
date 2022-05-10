import mmap
import sys

# Get the data from the file
with open(sys.argv[1], 'r') as f:
    m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
    data = m.readline().split()
    data = [int(x) for x in data]

# Find the minimum and maximum
print min(data), max(data)
