import mmap
# Test mmap.mmap(fileno=<fd>, length=(max_size+1))
buf = mmap.mmap(fileno=fd, length=max_size+1)
assert buf.size() == max_size+1

# Test mmap.mmap(-1, <max_size+1>)
buf = mmap.mmap(-1, max_size+1)
assert buf.size() == max_size+1

# Test mmap.mmap(-1, <max_size+1>, flags=mmap.MAP_SHARED)
buf = mmap.mmap(-1, max_size+1, flags=mmap.MAP_SHARED)
assert buf.size() == max_size+1

os.unlink(TMPFILE)
