import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expect <code>a</code> to be <code>b'\x01'</code>, but it is <code>b''</code>.
Thanks.


A:

The problem is that the file size is zero after the <code>truncate()</code> call and the <code>mmap</code> object is still using the old size.
The documentation says:
<blockquote>
<p>If <code>&lt;code&gt;length&lt;/code&gt;</code> is larger than the current size of the file, the file is extended with null bytes.</p>
</blockquote>
So, you can do:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate(1)
    a = m[:]
</code>

