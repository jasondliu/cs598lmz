import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # raises ValueError
</code>
My question is, why does this raise a <code>ValueError</code>? I don't see any mention of this in the docs. (I'm using Python 3.4.3 on Ubuntu 14.04)


A:

The problem is that the <code>mmap</code> object is not updated when you truncate the file.
From the docs:
<blockquote>
<p>The mmap object is mutable and may be modified in place, but modifications to the underlying file don’t appear in the mmap object and vice versa.</p>
</blockquote>
The <code>ValueError</code> is raised because the mmap object tries to access the bytes at the end of the file, which are no longer there.

