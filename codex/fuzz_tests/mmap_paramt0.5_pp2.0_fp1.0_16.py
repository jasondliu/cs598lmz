import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.close()
</code>
The first write works, but the second write doesn't.
I have tried using <code>mmap.ACCESS_WRITE</code> and <code>mmap.ACCESS_COPY</code> but no luck.
I'm using Python 3.5 on Linux.
EDIT:
I found that this works:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    m.write(bytes(2))
    m.close()
</code>
But I don't understand why.


A:

The documentation says:
<blockquote>
<p>The file’s current position is used as the starting point for the mapping; to map a file starting at a specific position, use <code>&lt;code&gt;seek()&lt;/code&gt;</code> to set the file’s current position before calling <code>&lt;code&gt;
