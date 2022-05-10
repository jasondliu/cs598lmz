import mmap
# Test mmap.mmap(-1, size)

# Try to create a file of size size
try:
    f = open("test.dat", "wb")
except IOError:
    print("Can't open file for writing")
    sys.exit(1)

# Try to create a file of size size
try:
    f = open("test.dat", "wb")
except IOError:
    print("Can't open file for writing")
    sys.exit(1)

try:
    f.write(b'\0' * size)
except MemoryError:
    print("Can't allocate that much memory")
    sys.exit(1)

f.close()

# Try to mmap the file of size size
try:
    m = mmap.mmap(-1, size)
except ValueError:
    print("mmap.mmap(-1, %d) failed" % size)
    sys.exit(1)

# Try to write to the mmap'ed region
try:
    m.write(b'\0' * size)
except MemoryError:
    print
