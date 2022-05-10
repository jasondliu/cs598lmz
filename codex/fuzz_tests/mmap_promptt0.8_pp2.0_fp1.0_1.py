import mmap
# Test mmap.mmap with the size parameter.

# Create a file and write 1Mb to it.
f = open("testfile", "w+")
for x in range(1024):
    f.write("abcd\n")
f.flush()


# Map the file in memory.
m = mmap.mmap(f.fileno(), 1048576, mmap.ACCESS_READ)

# Make sure it worked -- single-byte reads should work.
for x in range(1024):
    assert m[x*5] == 'a'
    assert m[x*5+1] == 'b'
    assert m[x*5+2] == 'c'
    assert m[x*5+3] == 'd'
    assert m[x*5+4] == '\n'


# Success.
print "Success."
