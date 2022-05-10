import mmap
# Test mmap.mmap (or mmap.mmap if you're on Python <3.3)
# It should implement the buffer protocol, i.e. support the
# 'memoryview' function:
d = mmap.mmap(-1, 16)
m = memoryview(d)
# And now 'm' should be the same as 'd' (except for the type):
assert(len(m) == 16)
# Make sure you can read from it:
assert(m[0] == 0)
# But you can't write to it:
#m[0] = 1 # this should fail
# Just to show that it's not any buffer, but a memoryview:
m.release() # this should fail too
# Now create a memoryview of a python object:
l = [1, 2, 3]
m = memoryview(l)
assert(len(m) == 3)
assert(m[0] == 1)
# but you can't write to it:
