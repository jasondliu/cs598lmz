import mmap
# Test mmap.mmap(fileno, length)
with open(os.path.join(os.getcwd(), 'mmap.mmap.txt'), 'w+') as f:
    f.write('foobar')
    f.flush()
    m = mmap.mmap(f.fileno(), 6)
    # Test mmap.write()
    m.write(b'baz')
    # Test mmap.seek()
    m.seek(0)
    # Test mmap.read()
    assert m.read(3) == b'baz'
    # Test mmap.readline()
    assert m.readline() == b'bar'
    # Test mmap.readlines()
    assert m.readlines() == []
    # Test mmap.tell()
    assert m.tell() == 6
    # Test mmap.flush()
    m.flush()
    # Test mmap.close()
    m.close()
