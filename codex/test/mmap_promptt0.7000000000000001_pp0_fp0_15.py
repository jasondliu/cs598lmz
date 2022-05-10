import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED, fd, 0)
with open("tmp_file", "w+b") as f:
    # Write a byte to the file
    f.write(b"\00")
    # Open the mmap
