import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))

with open('test', 'rb') as f:
    print(f.read())
</code>
The output is <code>b'\x00'</code> instead of <code>b'\x02'</code>. Why is that?

