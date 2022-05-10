import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'2'
    print(f.read())
    print(m[0])
    print(m[:])
    print(m[0:1])
    print(m[1:2])

m.close()
</code>
Prints:
<code>2
2
b'2\x00'
b'2'
b'\x00'
</code>

