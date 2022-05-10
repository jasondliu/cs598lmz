import mmap
# Test mmap.mmap.write_byte
size = mmap.PAGESIZE * 3
map = mmap.mmap(-1, size, flags=mmap.MAP_SHARED, tagname="TestSparseMap")
# Make sure the map is sparse.
offset = 0
while offset < size:
    map.write_byte(offset, b'x')
    offset += mmap.PAGESIZE * 2

# Try to write a byte at offsets that straddle a page boundary.
offset = mmap.PAGESIZE - 1
while offset < size - 2:
    # Try to write a byte at offsets that straddle a page boundary.
    map.write_byte(offset, b'x')
    offset += mmap.PAGESIZE * 2

# Make sure the map is sparse.
offset = 0
while offset < size:
    map.seek(offset)
    assert map.read_byte() == ord(b'x')
    offset += mmap.PAGESIZE * 2
