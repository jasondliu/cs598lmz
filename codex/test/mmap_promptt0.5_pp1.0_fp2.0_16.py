import mmap
# Test mmap.mmap() instead of mmap.mmap(fileno=0) to avoid a deadlock
# when the file is opened with fdopen() with the 'universal newlines'
# mode.  See http://bugs.python.org/issue5679.
m = mmap.mmap(0, 0, mmap.MAP_PRIVATE)
m.write(b"\n")
m.seek(0)
m.readline()
m.close()

# Test mmap.mmap(-1, ...)
m = mmap.mmap(-1, 1)
m.write(b"\n")
m.seek(0)
m.readline()
m.close()

# Test mmap.mmap(..., -1)
m = mmap.mmap(0, -1)
m.write(b"\n")
m.seek(0)
m.readline()
m.close()

