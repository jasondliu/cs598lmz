import mmap
# Test mmap.mmap()
try:
    with open('/dev/null', 'w') as f:
        f.write('foo')
except IOError:
    pass
else:
    raise RuntimeError('mmap.mmap() failed to raise IOError')
# Test mmap.mmap(fileno)
try:
    with open('/dev/null', 'w') as f:
        mmap.mmap(f.fileno())
except IOError:
    pass
else:
    raise RuntimeError('mmap.mmap(fileno) failed to raise IOError')
# Test mmap.mmap(fileno, length)
with open('/dev/null', 'w') as f:
    f.write('foo')
    mm = mmap.mmap(f.fileno(), 2)
    assert mm.read(2) == 'fo'
# Test mmap.mmap(-1, length)
mm = mmap.mmap(-1, 2)
assert mm.read(2) == '\x00\x00'
# Test mmap.mmap(fileno,
