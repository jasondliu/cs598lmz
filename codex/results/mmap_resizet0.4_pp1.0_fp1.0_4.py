import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises a <code>ValueError: mmap offset is greater than file size</code>.
It looks like the problem is that the <code>mmap</code> object has a cached size that is not updated when the file is truncated.
Is there a way to work around this?

