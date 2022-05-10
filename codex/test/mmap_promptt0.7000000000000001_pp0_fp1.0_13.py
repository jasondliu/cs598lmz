import mmap
# Test mmap.mmap
f = open(os.devnull, "r+b")
m = mmap.mmap(f.fileno(), 1)
m.write(b"A")
m.seek(0)
print(m.read())
print(m.size() == 1)
m.close()

# Test mmap.mmap.size()
f = open(os.devnull, "r+b")
m = mmap.mmap(f.fileno(), 0)
print(m.size() == 0)
m.close()

# Test mmap.mmap.flush()
f = open(os.devnull, "r+b")
m = mmap.mmap(f.fileno(), 1)
m.write(b"A")
m.flush()
m.close()

# Test mmap.mmap.close()
f = open(os.devnull, "r+b")
m = mmap.mmap(f.fileno(), 1)
m.close()

