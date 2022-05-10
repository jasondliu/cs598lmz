import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
accessing m[:] throws an <code>OSError: [Errno 21] Is a directory</code>. Is there a way to get the data that was previously mmapped before the truncate?

