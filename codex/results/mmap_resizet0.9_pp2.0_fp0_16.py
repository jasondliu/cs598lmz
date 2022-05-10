import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Real file size is 1 byte but <code>a</code> contains <code>b''</code>.
Why?


A:

From the doc at https://docs.python.org/3/library/mmap.html#mmap.mmap.read
<blockquote>
<p>If a change is made to the underlying file by some other process (using ftruncate(), for example), the mmap object is no longer usable, and an exception is raised.</p>
</blockquote>

