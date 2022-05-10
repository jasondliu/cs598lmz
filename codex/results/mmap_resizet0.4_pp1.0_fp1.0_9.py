import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expect the last line to raise <code>ValueError: mmap offset is greater than file size</code>, but it returns <code>b''</code> instead.
I'm using Python 3.6.8 on Windows 10.

