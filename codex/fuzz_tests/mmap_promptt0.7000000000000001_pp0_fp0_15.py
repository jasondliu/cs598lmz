import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED, fd, 0)
with open("tmp_file", "w+b") as f:
    # Write a byte to the file
    f.write(b"\00")
    # Open the mmap
    with mmap.mmap(f.fileno(), 1, prot=mmap.PROT_READ) as m:
        # Read the byte back
        print(m.read(1))
</code>

