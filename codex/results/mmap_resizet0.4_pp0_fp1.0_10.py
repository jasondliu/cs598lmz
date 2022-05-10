import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    print(a)
</code>
It's not clear to me why this works.  I would expect that the <code>mmap</code> object would be invalidated when the file is truncated.  But it seems to work.  Is this documented anywhere?  Is it portable?  Is it safe?


A:

This is documented in the <code>mmap</code> module documentation:
<blockquote>
<p>If the file is resized or otherwise modified, the <code>&lt;code&gt;mmap&lt;/code&gt;</code> object is updated to reflect the changes.</p>
</blockquote>
This is also portable, as it's the same behavior on Linux and Windows, and I'd expect it to be the same on other POSIX systems.
It's safe, as long as you don't try to read from the <code>mmap</code> object after the file has been closed.

