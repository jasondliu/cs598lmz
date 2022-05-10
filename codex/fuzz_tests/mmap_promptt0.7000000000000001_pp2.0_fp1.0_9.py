import mmap
# Test mmap.mmap()
def test_mmap():
    f = open('/tmp/mmaptest', 'w+b')
    try:
        f.seek(mmap.ALLOCATIONGRANULARITY * 2 - 1)
        f.write('\x00')
        f.seek(0)
        m = mmap.mmap(f.fileno(), mmap.ALLOCATIONGRANULARITY)
        m.write('foo')
        m.seek(0)
        s = m.read(3)
        assert s == 'foo'
    finally:
        m.close()
        f.close()
        os.unlink('/tmp/mmaptest')

def test_move():
    import mmap
    f = open('/tmp/mmaptest', 'w+b')
    try:
        f.write('\x00' * mmap.ALLOCATIONGRANULARITY)
        f.seek(0)
        m = mmap.mmap(f.fileno(), mmap.ALLOCATIONGRANULARITY)
        m.move(
