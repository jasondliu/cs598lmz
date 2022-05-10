import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    f.write(bytes(2))
    f.write(a)
</code>

<code>with open('test', 'rb') as f:
    assert f.readall() == b'\x01\x02'
</code>

