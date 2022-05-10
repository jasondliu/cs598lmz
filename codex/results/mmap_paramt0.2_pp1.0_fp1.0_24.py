import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read())

with open('test', 'rb') as f:
    print(f.read())
</code>
Output:
<code>b'\x02'
b'\x02'
</code>

