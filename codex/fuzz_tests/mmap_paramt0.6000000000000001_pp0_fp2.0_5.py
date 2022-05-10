import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(2)
    m.close()

with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[:])
    m.close()
</code>
Output:
<code>b'\x01\x00'
</code>

