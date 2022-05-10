import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[:])


with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.readline())
</code>
The output is:
<code>b'\x01'
b''
</code>
The second call to <code>readline()</code> should return the same data as the first call to <code>__getitem__()</code>. What's going on here?

