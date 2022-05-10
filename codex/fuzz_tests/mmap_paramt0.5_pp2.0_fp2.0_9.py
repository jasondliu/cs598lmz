import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    print(m.read(1))
    m.close()

with open('test', 'r+b') as f:
    print(f.read(1))
</code>
Output
<code>b'\x02'
b'\x02'
</code>
This is the same as doing this:
<code>with open('test', 'r+b') as f:
    f.write(bytes(2))
    print(f.read(1))

with open('test', 'r+b') as f:
    print(f.read(1))
</code>
Output
<code>b'\x02'
b'\x02'
</code>

