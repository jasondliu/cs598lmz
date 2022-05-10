import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0

with open('test', 'rb') as f:
    print(f.read())
</code>
This code prints <code>b'\x00'</code> as expected.

