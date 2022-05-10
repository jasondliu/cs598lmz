import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'1')
    m.seek(0)
    print(m.read(1))


with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read(1))
</code>

The output is:
<code>b'1'
b'1'
</code>

I expected the second read to return <code>b'\x01'</code>.
Why does it return <code>b'1'</code>?

