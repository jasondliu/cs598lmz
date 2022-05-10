import mmap
# Test mmap.mmap.read_byte() method.

# Open file for writing.
fd = os.open("bogus", os.O_CREAT | os.O_RDWR)

# Fill file with a few zeros.
os.write(fd, b"\x00" * 10)

# Create a mapping on the file.
m = mmap.mmap(fd, 10, access=mmap.ACCESS_READ)

# Read one byte from the beginning of the mapped region.
if m.read_byte(0) != 0:
    print("Couldn't read from mapped area")
    sys.exit(1)

print("mmap.mmap.read_byte() test passed.")
