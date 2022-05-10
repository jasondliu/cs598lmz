import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # mmap object has no attribute '__getitem__'
</code>
My expectation is that should read 1 as a result. I know it can be fixed with <code>m.close()</code> before <code>f.truncate()</code> but I am interested if there is another solution.


A:

It seems to be a bug in <code>mmap.mmap</code>. It can be fixed with:
<code>try:
    x = m[:]
except ValueError:
    pass
</code>

