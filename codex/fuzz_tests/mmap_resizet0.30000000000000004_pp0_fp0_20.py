import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expected the last line to raise an exception, but it doesn't. Why?


A:

The <code>mmap</code> object is not a view into the file, but a view into the memory-mapped file.
The memory-mapped file is a view into the file, but it is not updated when the file is truncated.

