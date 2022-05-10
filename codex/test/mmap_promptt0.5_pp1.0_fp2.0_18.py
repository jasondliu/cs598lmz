import mmap
# Test mmap.mmap() on a file opened with 'w+'

# This should create a file with 2 pages of zeroes

# This test is probably only valid on Windows, since the file
# is opened with O_RDWR, which on Unix would imply that the
# file is truncated to 0 length.  On Windows, the file is
# truncated to 0 length anyway, so it doesn't matter.

f = open("test.tmp", "w+")
f.write("\0" * 1024 * 1024)
f.close()

f = open("test.tmp", "w+")
f.write("\0" * 1024 * 1024)
f.close()

f = open("test.tmp", "w+")
m = mmap.mmap(f.fileno(), 1024 * 1024 * 2, access=mmap.ACCESS_WRITE)
m.write("hello")
m.close()

f = open("test.tmp", "r")
buf = f.read(1024 * 1024 * 2)
f.close()
