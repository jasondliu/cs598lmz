import mmap
# Test mmap.mmap with a zero-length file.

filename = os.path.join(support.TESTFN, "mmaptest")

# Open the file, write a byte to it, and close it.
# This creates a one-byte file.
f = open(filename, "wb")
f.write(b'a')
f.close()

# Open the file again and truncate it to zero length.
# This creates a zero-byte file.
f = open(filename, "wb")
f.truncate(0)
f.close()

# Open the file again with mmap.
m = mmap.mmap(f.fileno(), 0)

# Verify that we can read from the file.
m.seek(0)
print(m.read(1))

# Verify that we can write to the file.
m[0] = b'b'
m.seek(0)
