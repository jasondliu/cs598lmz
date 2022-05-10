import mmap
# Test mmap.mmap.read()
print "Memory mapped before:\n{}".format(mmap.mmap(fd, 0).read(100))

# Write bytes data
os.write(fd, b"aaaaaaaaaa")

# Flush the buffer of the file descriptor, so we can mmap.mmap.read() again
os.lseek(fd, 0, os.SEEK_SET)
print "Memory mapped after write:\n{}".format(mmap.mmap(fd, 0).read(100))

os.close(fd)

# Memory mapped file using "with"
with open('data', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print "Memory mapped:\n{}".format(m.read(100))
    m.close()
