import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line throws a <code>ValueError</code>. It seems that after a file was truncated, its mmap object is somehow invalidated and cannot be used anymore.
I am using Python 3.2.3.

