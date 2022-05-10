import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'a')
    m.write(b'b')
    m.write(b'c')
    m.seek(0)
    print(m.read(1))
    print(m.read(1))
    print(m.read(1))
    m.close()
</code>
This prints:
<code>b'a'
b'b'
b'c'
</code>

