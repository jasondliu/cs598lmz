import mmap
# Test mmap.mmap() with a file object.

with open('mmap_fileobj.dat', 'wb+') as f:
    f.write(b'foo')
    f.flush()
    m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
    assert m.read(3) == b'foo'
    m.close()

with open('mmap_fileobj.dat', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'bar')
    m.seek(0)
    assert m.read(3) == b'bar'
    m.close()

with open('mmap_fileobj.dat', 'r') as f:
    assert f.read() == 'bar'

try:
    with open('mmap_fileobj.dat', 'rb') as f:
        m = mmap.mmap(f.fileno(), 0)
        m.write(b'bar')
        m.seek(0)
       
