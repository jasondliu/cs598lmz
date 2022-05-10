import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
    m[0] = 0
    print(m[0])
    m.close()

with open('test', 'r+b') as f:
    print(f.read(1))
    print(f.read(1))
    print(f.read(1))
</code>
Output:
<code>b'\x01'
0
b'\x00'
b''
b''
</code>

