import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(2)
    m[1] = bytes(1)

with open('test', 'rb') as f:
    print(f.read())
</code>
output:
<code>b'\x01\x01'
</code>

