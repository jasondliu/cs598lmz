import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises a <code>ValueError</code> with the message <code>mmap offset is greater than file size</code>.
I would expect the <code>mmap</code> object to be updated to reflect the new file size.
Is there a way to do this without closing and reopening the file?


A:

The documentation for <code>mmap</code> says:
<blockquote>
<p>The size of the mapped region must not be zero, and it must be a multiple of the page size as returned by <code>&lt;code&gt;os.sysconf('SC_PAGE_SIZE')&lt;/code&gt;</code>.</p>
</blockquote>
So you can't truncate the file to zero bytes.

