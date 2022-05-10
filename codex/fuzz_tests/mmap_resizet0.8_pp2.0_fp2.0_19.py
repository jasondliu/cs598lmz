import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # segfault
</code>
The same code works fine on Windows. Is there anything I can do to make truncate() update the mmap object?


A:

This is a limitation of <code>mmap</code>.  From the docs:
<blockquote>
<p>If mmap() is used to map an empty file, the return address is unspecified.</p>
</blockquote>
On Linux, <code>mmap</code> appears to sometimes return the same address even if the file is truncated down to size 0.  On Windows, it seems to always return a different address when the file is truncated.  In any case, there is no guarantee that <code>mmap</code> will return a useful value for an empty file.  So you have to call <code>mmap</code> again.
This code seems to work on both platforms:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m = mmap.mmap(f.fileno(), 0)
