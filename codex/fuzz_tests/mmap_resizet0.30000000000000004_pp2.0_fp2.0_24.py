import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I thought that this should not happen, since the <code>mmap</code> object should be aware of the truncation.
I'm using Python 3.5.1 on Windows 7.

