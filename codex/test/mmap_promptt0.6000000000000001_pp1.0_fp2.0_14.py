import mmap
# Test mmap.mmap()

with open('/home/jmramoss/Downloads/test.txt', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde')
    m.seek(0)
    print(m.read(10))
    m.seek(0)
    print(m.read(10))
    m.close()

print('\n\n')

with open('/home/jmramoss/Downloads/test.txt', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write(b'abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde')
    m.seek(0)
    print(m.read(10))
