import mmap
# Test mmap.mmap()
# https://docs.python.org/3.4/library/mmap.html

import mmap

with open('test.txt', 'r+') as f:
    with mmap.mmap(f.fileno(), 0) as mm:
        while True:
            line = mm.readline().rstrip()
            if line == b'END':
                break
            print(line)

# Test mmap.mmap().move()
# https://docs.python.org/3.4/library/mmap.html

import mmap

buffer = mmap.mmap(-1, 100, tagname='mybuffer', access=mmap.ACCESS_WRITE)
buffer.move(0, 20, 60)
buffer.write(b'new contents for buffer')
buffer.close()

# Test mmap.mmap().find()
# https://docs.python.org/3.4/library/mmap.html

import mmap

with open('test.txt', 'r+') as f:
    with mmap.mmap(f
