import mmap
# Test mmap.mmap(fileno, length[, access[, offset]])
#
# Note that mmap is basically a wrapper for the mmap system call.
#
length = mmap.PAGESIZE
m = mmap.mmap(-1, length)
#
# Set all bytes to zero
#
m.write(b'\0' * length)
#
# Write the string at the beginning
#
m.seek(0)
m.write(b'Here is a bunch of text')
#
# Read it back
#
m.seek(0)
s = m.read(17)
m.close()
print(s)

# Test mmap.mmap(fileno, length[, tagname[, access[, offset]]])
#
# Note that mmap is basically a wrapper for the mmap system call.
#
length = mmap.PAGESIZE
m = mmap.mmap(-1, length, tagname='mmap_example')
#
# Set all bytes to zero
#
m.write(b'\0' * length)
#
# Write the
