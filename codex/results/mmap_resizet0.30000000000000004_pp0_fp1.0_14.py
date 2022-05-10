import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This is the output I get:
<code>b'\x00'
</code>
I would expect the output to be <code>b'\x01'</code>.
Why is this?

