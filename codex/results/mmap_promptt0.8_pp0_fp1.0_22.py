import mmap
# Test mmap.mmap().
with open('burke.htm', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(f'{len(m)} bytes')
    print(m[0:1000])
    print(repr(m[0:1000]))
    m.close()

import random
with open('burke.htm', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    for i in range(100000): n = random.randint(0, len(m) - 1000)
    m.seek(n)
    print(f'Starting at {n}')
    for i in range(10): print(m.readline().decode())
    m.close()
