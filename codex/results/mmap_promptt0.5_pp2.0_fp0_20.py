import mmap
# Test mmap.mmap
import mmap

def test_mmap():
    f = open('test.txt', 'w+')
    f.write('Hello World')
    f.close()

    f = open('test.txt', 'r+')
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    s = m.readline()
    assert s == 'Hello World'
    m.close()
    f.close()

    os.unlink('test.txt')

# Test mmap.mmap with offset and size
import mmap

def test_mmap_with_offset_and_size():
    f = open('test.txt', 'w+')
    f.write('Hello World')
    f.close()

    f = open('test.txt', 'r+')
    m = mmap.mmap(f.fileno(), 10, offset=6)
    m.seek(0)
    s = m.readline()
    assert s == 'World'
    m.close()
    f.close()
