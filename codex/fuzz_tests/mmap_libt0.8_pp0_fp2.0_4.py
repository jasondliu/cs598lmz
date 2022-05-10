import mmap
with open('name.txt', 'wb') as f:
    f.write(b'hello')
with open('name.txt', 'r') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    if m.find(b'hello') != -1:
        print('true')
    else:
        print('false')
m.close()
with open('name.txt', 'w') as f:
    f.write('world')
with open('name.txt', 'r') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    if m.find(b'hello') != -1:
        print('true')
    else:
        print('false')
m.close()

import mmap
with open('name.txt', 'wb') as f:
    f.write(b'hello')
with open('name.txt', 'r') as f:
    m = mmap.mmap(f.
