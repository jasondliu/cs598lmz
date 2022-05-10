import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0
</code>
The same code with "rb" mode for open instead of "r+b" will give you
<blockquote>
<p>mmap.error: [Errno 1] Operation not permitted</p>
</blockquote>

