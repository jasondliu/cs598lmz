import mmap
import sys

# Create a memory-map to an array
filename = sys.argv[1]
size = os.path.getsize(filename)
f = open(filename, "rb")
mm = mmap.mmap(f.fileno(), size, access=mmap.ACCESS_READ)

# Read the entire content of the file at once
mm.readline()
print(mm.readline())
print(mm.readline())
mm.close()
f.close()
