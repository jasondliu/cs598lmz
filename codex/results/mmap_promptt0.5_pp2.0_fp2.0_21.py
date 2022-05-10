import mmap
# Test mmap.mmap.read_byte
m = mmap.mmap(0, 1, 'mmaptest')
m.write_byte(ord('a'))
assert m.read_byte() == ord('a')
m.close()
# Test mmap.mmap.readline
m = mmap.mmap(0, 1, 'mmaptest')
m.write_byte(ord('a'))
m.write_byte(ord('\n'))
m.write_byte(ord('b'))
m.write_byte(ord('\n'))
m.write_byte(ord('c'))
m.seek(0)
assert m.readline() == b'a\n'
assert m.readline() == b'b\n'
assert m.readline() == b'c'
m.close()
# Test mmap.mmap.read
m = mmap.mmap(0, 1, 'mmaptest')
m.write_byte(ord('a'))
m.write_byte(ord('\n'))
m.write_byte(
