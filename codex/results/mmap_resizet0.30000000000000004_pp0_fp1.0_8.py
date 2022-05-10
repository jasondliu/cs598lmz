import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I would expect this to raise an <code>IndexError</code> or <code>ValueError</code> or something, but it just returns an empty byte string.
I'm using Python 3.5.2 on Linux.


A:

The <code>mmap</code> object is not updated when the file is truncated.
The documentation says:
<blockquote>
<p>If the file on disk is resized by another process while it is open, the <code>&lt;code&gt;mmap&lt;/code&gt;</code> object will reflect the new size.</p>
</blockquote>
But it does not say anything about the file being truncated.

