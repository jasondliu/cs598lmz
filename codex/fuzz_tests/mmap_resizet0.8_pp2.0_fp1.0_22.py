import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
On <code>f.truncate()</code> it throws a <code>ValueError</code> exception with the following message:
<blockquote>
<p>ValueError: mmap can't extend a read-only or copy-on-write file</p>
</blockquote>
However when I remove <code>m[:]</code> (or change it to <code>m.read(1)</code>), there is no exception thrown.
What's the difference between these two ways to read the contents of the file?
Why does it throw the error when assigning to <code>a</code> but not when I call <code>m.read</code>?


A:

The problem is that <code>m[:]</code> is a slice of a slice, and all slicing in Python creates a copy, even if the slice is of a byte array.  So <code>m[:]</code> returns a new byte array, and the mmap object has no way of knowing that you then use that byte array.  The mmap object has been designed so that you only use
