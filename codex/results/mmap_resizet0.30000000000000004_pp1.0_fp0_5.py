import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get a <code>ValueError: mmap offset is greater than file size</code> on the last line.
I would expect the <code>mmap</code> to be updated when the file is truncated.
I am using Python 3.6.5.

