import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0
</code>
I get this error:
<code>TypeError: must be read-write buffer, not _mmap.mmap
</code>
If I try this:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(1))
</code>
I get:
<code>ValueError: mmap can't modify memory mapped using mmap(MAP_PRIVATE)
</code>
Thanks!


A:

The first code block doesn't work because <code>m</code> is a mmap object, not a writable buffer that can be used to set the value of <code>m[0]</code>.
The second code block doesn't work because you're calling <code>mmap.mmap</code> with <code>MAP_PRIVATE</code> (the default flag), which means you
