import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code> on the last line.
I understand that the file is empty, but why is the mmap object not updated?
I know I can use <code>m.resize()</code> to fix this, but I would like to understand why this is happening.
I am using Python 3.6.


A:

<code>mmap</code> is a wrapper around the C <code>mmap</code> function, which is documented as follows:
<blockquote>
<p>If the file is extended, the extra data is unspecified. If the file is shortened, the extra data is discarded.</p>
</blockquote>
This is a feature of the underlying system call, not a bug in Python.

