import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)

    print(m.read(1))

    m[0] = 48

with open('test', 'rb') as f:
    print(f.read(1))
</code>
Prints:
<code>b'\x01'
b'0'
</code>

