import mmap
# Test mmap.mmap
import mmap

def test_mmap_write():
    f = open('data.txt', 'w+')
    f.write('Hello Python!')
    f.close()
    f = open('data.txt', 'r+')
    m = mmap.mmap(f.fileno(), 0)
    m.write('Hello World!')
    m.seek(0)
    print m.read(13)
    m.close()
    f.close()

def test_mmap_read():
    f = open('data.txt', 'w+')
    f.write('Hello Python!')
    f.close()
    f = open('data.txt', 'r+')
    m = mmap.mmap(f.fileno(), 0)
    m.seek(6)
    print m.read(6)
    m.close()
    f.close()

def test_mmap_find():
    f = open('data.txt', 'w+')
    f.write('Hello Python!')
    f.close()

