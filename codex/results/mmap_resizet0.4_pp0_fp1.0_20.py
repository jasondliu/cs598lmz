import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I expected that <code>a</code> would contain <code>b'\x01'</code>.
Is this a bug in <code>mmap</code>?

I am using Python 3.6.6.

