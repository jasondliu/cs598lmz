import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[:])
    m[:] = bytes(0)
    print(m[:])
    m[:] = bytes(1)
    print(m[:])
    m[:] = bytes(2)
    print(m[:])
    m.close()
</code>
Output:
<code>b'\x01'
b'\x00'
b'\x01'
b'\x02'
</code>

