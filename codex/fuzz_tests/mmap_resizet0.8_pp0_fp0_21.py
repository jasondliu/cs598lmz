import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    # m[:] = b'0'
    # print(m[:])
</code>
Output:
<code>b'\x01'
</code>
Both the read and write work.

