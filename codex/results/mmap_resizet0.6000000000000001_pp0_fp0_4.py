import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This is on Python 3.4.3 on Ubuntu 14.04.4.


A:

The problem is that the <code>mmap</code> is still using the old file size, because it's not notified when the file size changes.
In fact, the documentation says:
<blockquote>
<p>It is also possible to create an <code>&lt;code&gt;mmap&lt;/code&gt;</code> object by using <code>&lt;code&gt;mmap.mmap()&lt;/code&gt;</code>
  to open an existing file. If the file is extended, the <code>&lt;code&gt;mmap&lt;/code&gt;</code> object
  can be resized using the <code>&lt;code&gt;mmap.resize()&lt;/code&gt;</code> method. If the file is
  reduced, the extra data in the <code>&lt;code&gt;mmap&lt;/code&gt;</code> object is discarded.</p>

