import mmap
# Test mmap.mmap(-1, 1).close()
with open("test.txt", "wb") as f:
    # Write two null bytes to the file.
    f.write(b'\x00\x00')
map = mmap.mmap(-1, 1)
map.close()
