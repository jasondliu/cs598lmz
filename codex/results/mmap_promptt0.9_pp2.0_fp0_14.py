import mmap
# Test mmap.mmap with read-only permissions

# It's important to open the file in binary mode, otherwise the
# behaviour of the fileops on the mapped region are undefined.
with open("temp", "sy") as f:
    with mmap.mmap(f.fileno(), 0) as m:
        print(m)

# Open the same file with write-permissions
with open("temp", "wsy") as f:
    with mmap.mmap(f.fileno(), 0) as m:
        print(m)
