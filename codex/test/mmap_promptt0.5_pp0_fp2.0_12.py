import mmap
# Test mmap.mmap()

# Test mmap.mmap()

def test_mmap():
    f = open('testfile', 'w+')
    f.write('hello world')
    f.close()
    f = open('testfile', 'r+')
    m = mmap.mmap(f.fileno(), 0)
    m.write('bye world')
    m.seek(0)
    m.readline()
    m.close()
    f.close()
    os.unlink('testfile')

test_mmap()
