import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b''</code> but I would expect it to be <code>b'\x01'</code>.
What is going on here?


A:

<code>mmap</code> is a memory-mapped file. It's not a cache of the file, it's a view of the file.
When you truncate the file, the file is truncated. The memory-mapped file is still there, but it's not a view of the file anymore. It's a view of the truncated file.

