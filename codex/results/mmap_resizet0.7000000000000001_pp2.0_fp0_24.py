import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This will also raise <code>ValueError: mmap offset is greater than file size</code>
But what I don't understand is why this error comes from <code>m[:]</code> and not from <code>f.truncate()</code>?

