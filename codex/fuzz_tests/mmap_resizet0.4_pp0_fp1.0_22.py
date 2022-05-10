import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I'd expect <code>a</code> to be an empty byte string, but it is actually <code>b'\x01'</code>. Why is that?


A:

From the docs:
<blockquote>
<p>The <code>&lt;code&gt;mmap()&lt;/code&gt;</code> function may need to increase the size of the underlying file. <strong>If the file is not large enough, calls to <code>&lt;code&gt;mmap()&lt;/code&gt;</code> will fail with <code>&lt;code&gt;ENOMEM&lt;/code&gt;</code></strong> until the file is made larger.</p>
</blockquote>
So, if you want to truncate the file, you should do it before calling <code>mmap()</code>.

