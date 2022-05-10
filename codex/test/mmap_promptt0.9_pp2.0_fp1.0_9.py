import mmap
# Test mmap.mmap and mmap.ACCESS_WRITE

try:
    f = open("foo.txt", "r+b")
except IOError:
    print("Could not open file. Terminating")
    sys.exit(1)

#
# The map is writable by default.
# Setting access=mmap.ACCESS_WRITE causes mmap
# to raise an exception.
#
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
print("Closing fd used by the mapping object")
del f
try:
    print("Trying to read the file with the mapping object...")
    print(m.readline())
except Exception:
    print("Readline failed")
else:
    print("Readline successful")
try:
    print("Trying to write the file with the mapping object...")
    m.write("foo")
except Exception:
    print("Write failed")
else:
    print("Write successful")

print("Unmapping the file.\n")
m.close()
