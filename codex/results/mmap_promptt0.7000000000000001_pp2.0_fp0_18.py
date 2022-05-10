import mmap
# Test mmap.mmap.write_byte with 0 <= pos < len(mmap)

with open('temp', 'w+t') as f:
    f.write('abcde')

with open('temp', 'r+t') as f:
    m = mmap.mmap(f.fileno(), 5)
    for i in range(5):
        m.write_byte(i, 'X')
        m.seek(0)
        assert m.read(5) == 'X' * 5
        m.seek(i)
    m.close()

with open('temp', 'r+t') as f:
    assert f.read() == 'X' * 5

# Test mmap.mmap.write_byte with pos < 0 and pos > len(mmap)

with open('temp', 'w+t') as f:
    f.write('abcde')

with open('temp', 'r+t') as f:
    m = mmap.mmap(f.fileno(), 5)
    m.write_byte(-1, 'X')
    m.
