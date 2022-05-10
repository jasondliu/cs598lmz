import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(4)
</code>
This works well, but in the real program, I need to write bytes object of arbitrary length.
The only way I found is:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[len(m):] = b'Some bytes'
    m.resize(len(m) + len(b'Some bytes'))
</code>
But this is not efficient, because it rewrites all the memory. Is there a better way?

