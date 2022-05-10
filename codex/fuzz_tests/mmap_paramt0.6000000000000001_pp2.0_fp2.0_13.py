import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.move(0, 1, 1)
    m.close()

with open('test', 'rb') as f:
    print(repr(f.read()))
</code>
Output:
<code>b'\x00'
</code>
I would expect the resulting file to be <code>b'\x01'</code>

