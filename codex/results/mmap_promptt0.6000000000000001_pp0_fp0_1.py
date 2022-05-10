import mmap
# Test mmap.mmap.read_byte
m = mmap.mmap(-1, 1)
m.write_byte(b'A')
m.seek(0)
assert m.read_byte() == b'A'
assert m.read_byte() == b''
m.close()
# Test mmap.mmap.readline
m = mmap.mmap(-1, 1)
m.write(b'A\n')
m.seek(0)
assert m.readline() == b'A\n'
assert m.readline() == b''
m.close()

# Test mmap.mmap with a file
with open('test.txt', 'w+') as f:
    f.write('hello')
    f.flush()
    with mmap.mmap(f.fileno(), 0) as m:
        assert m.read_byte() == b'h'
        assert m.read_byte() == b'e'
        assert m.read_byte() == b'l'
        assert m.read_byte() == b'l'
        assert m
