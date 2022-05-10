import mmap
# Test mmap.mmap.tell()

with open(test.test_support.TESTFN, 'wb') as f:
    f.write(b'\0' * 100)
with open(test.test_support.TESTFN, 'rb') as f:
    m = mmap.mmap(f.fileno(), 100)
    m.seek(50)
    if m.tell() != 50:
        raise ValueError('tell: expected 50, got %d' % m.tell())
    m.close()

# Test that mmap.mmap.tell() raises a ValueError if the mmap object is closed
with open(test.test_support.TESTFN, 'wb') as f:
    f.write(b'\0' * 100)
with open(test.test_support.TESTFN, 'rb') as f:
    m = mmap.mmap(f.fileno(), 100)
    m.close()
    try:
        m.tell()
    except ValueError:
        pass
    else:
        raise ValueError('Expected ValueError')
