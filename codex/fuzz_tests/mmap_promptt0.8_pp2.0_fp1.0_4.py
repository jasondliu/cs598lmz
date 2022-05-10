import mmap
# Test mmap.mmap
with open('test.txt', 'wb') as f:
    f.write('abcd')
with open('test.txt', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print 'Before:', m.readline()
    m.seek(0)
    m.write('efgh')
    m.seek(0)
    print 'After:', m.readline()
os.remove('test.txt')
