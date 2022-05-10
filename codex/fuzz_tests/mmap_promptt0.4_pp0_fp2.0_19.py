import mmap
# Test mmap.mmap(0, 1)
# On Windows, this is a 64K region, and the 0xFF bytes are not written.
# On Linux, this is a 4096 byte region, and the 0xFF bytes are written.
# On MacOS, this is a 4096 byte region, and the 0xFF bytes are written.

# On Windows, use the following:
# fd = os.open(r"\\.\PhysicalDrive0", os.O_RDWR)

# On Linux, use the following:
# fd = os.open("/dev/sda", os.O_RDWR)

# On MacOS, use the following:
# fd = os.open("/dev/disk0", os.O_RDWR)

fd = os.open("/dev/sda", os.O_RDWR)

m = mmap.mmap(fd, 1)

# This is the actual test.
m[0] = 0xFF

m.close()
os.close(fd)

# On Windows, this will fail with:
#   WindowsError: [Error
