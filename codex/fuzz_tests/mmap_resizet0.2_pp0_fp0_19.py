import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line throws <code>ValueError: mmap offset is greater than file size</code>.
I understand that the file is truncated, but the mmap object is still valid.
Why is this happening?
How can I fix it?

