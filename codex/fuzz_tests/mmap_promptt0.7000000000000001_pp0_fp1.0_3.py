import mmap
# Test mmap.mmap.flush()
try:
    mmap.mmap(0, 10).flush()
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test mmap.mmap.tell()
try:
    mmap.mmap(0, 10).tell()
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test mmap.mmap.seek()
try:
    mmap.mmap(0, 10).seek(0)
except AttributeError:
    print('SKIP')
    raise SystemExit

m = mmap.mmap(0, 10)
m.seek(0)
print(m.tell() == 0)
m.seek(1)
print(m.tell() == 1)
m.seek(0, 2)
print(m.tell() == 0)
m.seek(1, 2)
print(m.tell() == 1)
