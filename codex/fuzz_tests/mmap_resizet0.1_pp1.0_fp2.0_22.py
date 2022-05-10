import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line throws <code>ValueError: mmap offset is greater than file size</code>.
I understand that the file size is 0, but I don't understand why the offset is 1.
I'm using Python 3.6.5 on Windows 10.


A:

The problem is that the <code>mmap</code> object is not updated when the file is truncated.
The documentation says:
<blockquote>
<p>The mmap object is not updated if the underlying file on disk is changed by another process. To update the mmap object, use the <code>&lt;code&gt;mmap.resize()&lt;/code&gt;</code> method.</p>
</blockquote>
So, you can fix your code by adding <code>m.resize(0)</code> after <code>f.truncate()</code>.

