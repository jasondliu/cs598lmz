import mmap
# Test mmap.mmap(fileno, length, access=ACCESS_DEFAULT, offset=0, *, tagname=None, file_like=False)
# for the following file.
#
# 1. When tagname is not specified.
# 2. When tagname is specified.
#
# Also, test the following access modes.
#
# 1. ACCESS_READ
# 2. ACCESS_WRITE
# 3. ACCESS_COPY
# 4. ACCESS_DEFAULT
#

def test_mmap_file(access_mode, tagname):
    # Generate test file.
    with open("test_mmap_file.txt", "w") as f:
        for i in range(0, 1024):
            f.write("%s\n" % (i))

    # Open test file and get file descriptor.
    fd = os.open("test_mmap_file.txt", os.O_RDWR)

    # Create a memory map.
    m = mmap.mmap(fd, 1024, access_mode, 0, tagname=tagname)


