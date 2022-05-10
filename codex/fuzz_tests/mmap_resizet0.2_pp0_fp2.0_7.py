import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line gives me a <code>ValueError</code>:
<code>ValueError: mmap offset is greater than file size
</code>
I was expecting <code>a</code> to be <code>b''</code>.
Why does this happen?

