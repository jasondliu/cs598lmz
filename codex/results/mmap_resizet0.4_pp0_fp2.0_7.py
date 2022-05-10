import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
But if I change <code>f.truncate()</code> to <code>f.truncate(0)</code> it works fine.
Why is that?


A:

The documentation for <code>mmap.mmap</code> states:
<blockquote>
<p>If length is omitted, the maximum length possible is used: usually, this is the remainder of the file starting at offset.</p>
</blockquote>
So your <code>mmap</code> object is trying to access the entire file, which is now 0 bytes long.

