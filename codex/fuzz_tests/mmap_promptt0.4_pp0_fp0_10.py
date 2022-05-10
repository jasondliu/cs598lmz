import mmap
# Test mmap.mmap.read_byte

# Read a byte from a memory-mapped file
with open("example_file.bin", "r+b") as f:
    # Memory-map the file, size 0 means whole file
    m = mmap.mmap(f.fileno(), 0)
    # Read the first byte
    byte = m.read_byte()
    print(byte)
    # Update the first byte
    m.seek(0)
    m.write_byte(b'B')
    m.flush()
    m.seek(0)
    byte = m.read_byte()
    print(byte)
    # Close the map
    m.close()
