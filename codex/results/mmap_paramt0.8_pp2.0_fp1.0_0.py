import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = str(2)

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    b = m[:]

with open('test', 'rb') as f:
    print(f.read())
</code>
Running this code prints <code>b'2'</code> which is what we expect.

