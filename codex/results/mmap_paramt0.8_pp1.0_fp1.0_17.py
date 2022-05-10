import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.resize(5)
    print(m.read(5))

    m.seek(0)
    m.write(b'1234')
    m.close()
</code>
outputs
<code>b'\x01\x00\x00\x00\x00'
</code>

