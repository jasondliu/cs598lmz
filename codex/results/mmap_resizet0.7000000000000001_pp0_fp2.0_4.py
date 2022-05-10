import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)

with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    print(a)
</code>
OUTPUT:
<code>b''
b'\x01'
</code>

