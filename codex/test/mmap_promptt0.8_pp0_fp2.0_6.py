import mmap
# Test mmap.mmap.write_byte and mmap.mmap.write
x = mmap.mmap(-1, 3)
x.write_byte('a')
x.write_byte('b')
x.write_byte('c')
x.seek(0)
assert x.read_byte() == 'a'
assert x.read_byte() == 'b'
assert x.read_byte() == 'c'

x = mmap.mmap(-1, 3)
x.write('xyz')
x.seek(0)
assert x.read(3) == 'xyz'

x = mmap.mmap(-1, 6)
x.write_byte('a')
x.write_byte('b')
x.write_byte('c')
x.write_byte('d')
x.write_byte('e')
x.write_byte('f')
x.seek(2,1)
assert x.read_byte() == 'd'

x = mmap.mmap(-1, 6)
