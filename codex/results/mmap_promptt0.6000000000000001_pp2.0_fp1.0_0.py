import mmap
# Test mmap.mmap for read and write.

def main():
    f = open('mmap.txt', 'w+')
    f.write('Hello, world!')
    f.close()
    f = open('mmap.txt', 'r+')
    m = mmap.mmap(f.fileno(), 0)
    print 'Before:', m.readline()
    m.seek(0)
    m.write('Hi there!')
    m.seek(0)
    print 'After:', m.readline()
    m.close()
    f.close()

if __name__ == '__main__':
    main()
