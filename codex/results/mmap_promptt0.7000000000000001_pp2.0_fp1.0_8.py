import mmap
# Test mmap.mmap(fileno, length, access=ACCESS_READ|ACCESS_WRITE, offset=0)

def test(name, file, size, access):
    print name, '-',
    f = open(file, 'r+')
    m = mmap.mmap(f.fileno(), size, access)
    f.close()
    m.close()

try:
    test('read-only', '/dev/zero', 1, mmap.ACCESS_READ)
    test('read-write', '/dev/zero', 1, mmap.ACCESS_WRITE)
    test('read-copy', '/dev/zero', 1, mmap.ACCESS_COPY)
    print 'ok'
except:
    print 'failed'
