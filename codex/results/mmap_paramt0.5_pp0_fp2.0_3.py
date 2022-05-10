import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
    m[0] = bytes([0])
    print(m[0])

with open('test', 'rb') as f:
    print(f.read())
</code>
The output is:
<code>b'\x01'
b'\x00'
b'\x00'
</code>

