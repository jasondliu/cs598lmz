import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'2'


with open('test', 'r+b') as f:
    m=mmap.mmap(f.fileno(), 0)
    m[:]= b'\x42\x00\x08'

with open('test', 'rb') as f:
    m= mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    all_zeros= not any(m)

with open('test', 'rb') as f:
    m=mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    print(all(m))

with open('test', 'rb') as f:
    m=mmap.mmap(f.fileno(), 0, access =mmap.ACCESS_WRITE)
    m.fini()

import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))
    f.write(bytes(3))

with open('test
