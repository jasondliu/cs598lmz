import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I'm trying to use memory-mapping to read a file that is being truncated. I'm getting an <code>IndexError: string index out of range</code> on the <code>m[:]</code> line. I'm not sure if this is because the file is being truncated while I'm reading it, or if I'm doing something else wrong.
I'm using Python 3.6.5 on Ubuntu 18.04.


A:

<blockquote>
<p>I'm trying to use memory-mapping to read a file that is being truncated.</p>
</blockquote>
You can't do that.
<code>mmap</code> is not a general-purpose file abstraction.  It's a way of mapping a file into the process's address space.  If the file size changes, the mapping may no longer be valid.
You can't use <code>mmap</code> to read a file that is being truncated.  (Or written to, or deleted, or moved, or ...)

