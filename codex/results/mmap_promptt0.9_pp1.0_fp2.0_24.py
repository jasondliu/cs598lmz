import mmap
# Test mmap.mmap()
# - write to it
# - mmap.find
# - mmap.rfind
# - mmap.flush
print "Test mmap.mmap()"
f = open("mmaptest", "wb+")
f.write("x" * mmap.PAGESIZE)
m = mmap.mmap(f.fileno(), mmap.PAGESIZE)
m.write("1234567890abcdef")
assert m.find("345") == 3
assert m.rfind("456") == 4
m.flush()
m.seek(0,0)
assert m.find("345") == 3
assert m.find("xyz") == -1
m.close()
f.close()

# Test mmap.mmap(-1, ...)
# - write to it
# - mmap.find
# - mmap.rfind
# - mmap.flush
print "Test mmap.mmap(-1)"
f = open("mmaptest", "wb+")
m = mmap.mmap(f.fileno(), 0)
m.write
