import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)

    m[0] = 0
</code>
That works.
But if I use <code>mmap.ACCESS_COPY</code>
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY)

    m[0] = 0
</code>
I get an error:
<code>mmap.error: [Errno 22] Invalid argument
</code>
Why?


A:

From the documentation:
<blockquote>
<p>ACCESS_COPY:    Create a private copy-on-write mapping.</p>
</blockquote>
I.e. the memory map is not backed by the file. Any changes are written back to the file only when the memory map is closed.

