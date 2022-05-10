import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
If I print <code>a</code> I get <code>b'\x01'</code>. The documentation says:
<blockquote>
<p>If the file is opened for read/write access, this method does not
  truncate the file to the specified size, but only sets the file’s size
  to the specified size. The file’s current position isn’t changed.</p>
</blockquote>
So the <code>mmap</code> should be still valid. But if I want to access <code>m[0]</code> I get <code>ValueError: mmap offset is greater than file size</code>. Why? I'm using Python 3.7.
I can't even do this:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I get the same error.

