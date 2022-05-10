import mmap
# Test mmap.mmap.read()
def test_read(size, offset, fname):
    with open(fname, 'r+b') as f:
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
            print('Memory mapped file:')
            print(m.read(size))
            m.seek(offset)
            print('Memory mapped file:')
            print(m.read(size))

# Test mmap.mmap.write()
def test_write(size, offset, fname):
    with open(fname, 'r+b') as f:
        with mmap.mmap(f.fileno(), 0) as m:
            print('Before:\n{}'.format(m.read(size)))
            m.seek(offset)
            m.write(b'abcdefghijklmnop')
            m.seek(0)
            print('After:\n{}'.format(m.read(size)))

# Test mmap.mmap.move()
def test_move(size,
