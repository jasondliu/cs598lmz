import mmap
# Test mmap.mmap.write_byte()

# This test is not automated because it requires a human to confirm that
# the correct byte was written to the file.

# Create a file and write a single byte to it
with open("mmap_write_byte.txt", "wb") as f:
    f.write(b"a")

# Open the file for reading and writing, and memory map it
with open("mmap_write_byte.txt", "r+b") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    print("Before:")
    print(m.read(1))

    # Write a new byte to the file
    m.write_byte(b"b")
    m.seek(0)

    print("After:")
    print(m.read(1))
