import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # &lt;- returns b''
</code>
A workaround is to use <code>mmap.resize</code> before <code>truncate</code>.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    mmap.resize(m, 1)
    f.truncate()
    a = m[:]  # &lt;- returns b'\x00'
</code>
Is this a bug or a feature?

Note, there is a similar question, but it is about <code>mmap.resize</code> and <code>truncate</code> in reverse order.


A:

I think that it is a bug.
The documentation for <code>mmap.resize</code> says:
<blockquote>
<p>The size of the mapped region must remain less than or equal to the size of the underlying file.</p>
</blockquote>
