import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expected that <code>a</code> would be <code>b''</code>, but it is <code>b'\x01'</code>.
If I change the <code>f.truncate()</code> to <code>m.resize(0)</code>, then <code>a</code> is <code>b''</code>.
I am using Python 3.6.2 on Windows 10.
Why does <code>f.truncate()</code> not work, and why does <code>m.resize(0)</code> work?


A:

<code>f.truncate()</code> is not guaranteed to change the size of the underlying file.  It is only guaranteed to change the size of the file as reported by <code>f.seek(0, 2)</code>.  The documentation says:
<blockquote>
<p>Truncate the file’s size. If the optional size argument is present, the file is truncated to (at most) that size. The size defaults to the current position. The current file position is not changed.</p
