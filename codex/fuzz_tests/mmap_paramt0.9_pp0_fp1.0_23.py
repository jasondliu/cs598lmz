import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    print(m[0], 'should be 49 (the ASCII code for 1)')
    m[0] = 255
    m.flush()
    m.close()

with open('test', 'rb') as f:
    b = f.read()
    print(b, 'should be b\'\\xff\'')
</code>

