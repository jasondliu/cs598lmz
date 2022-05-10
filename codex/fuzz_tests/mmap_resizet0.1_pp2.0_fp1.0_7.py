import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that the file size is 0, but I don't understand why the offset is greater than the file size.
I'm using Python 3.6.1 on Windows 10.


A:

The problem is that the <code>mmap</code> object is not updated when the file is truncated.
The documentation says:
<blockquote>
<p>The mmap() function may need to update internal data structures to reflect the new size. To force this update to occur, call the <code>&lt;code&gt;mmap.resize()&lt;/code&gt;</code> method.</p>
</blockquote>
So, adding <code>m.resize(0)</code> before the <code>a = m[:]</code> line fixes the problem.

