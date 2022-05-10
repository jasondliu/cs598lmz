import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I thought that <code>f.truncate()</code> would cause <code>mmap.mmap</code> to raise an exception, but it actually returns the zero-length string <code>b''</code>.
What's going on here?


A:

<blockquote>
<p>What's going on here?</p>
</blockquote>
The <code>mmap.mmap</code> object is keeping track of the size of the file in its own way when you open it, and after you truncate the file it is still using that old size.  It is not keeping track of the file size in a way that would be affected by the <code>truncate()</code> method.
<blockquote>
<p>I thought that f.truncate() would cause mmap.mmap to raise an exception,</p>
</blockquote>
The <code>mmap</code> module documentation says:
<blockquote>
<p>If the file is resized, the changes do not appear in the mmap object
  until the next time it is accessed.</
