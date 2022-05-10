import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I thought that truncation does not change the file size and mmap will be valid.
Is it possible to avoid this error?

