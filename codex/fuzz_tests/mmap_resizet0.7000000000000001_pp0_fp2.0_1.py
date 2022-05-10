import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expect the last line to raise <code>mmap.error</code> but it returns the empty string <code>''</code>.
Why is that? Is the error ignored or does the memory map get updated when the file is truncated?


A:

The issue is that <code>mmap.mmap</code> does not raise an exception when the file is truncated. The documentation says that <code>mmap</code> objects support the buffer protocol, so that is probably the reason why <code>m[:]</code> returns the empty string.

