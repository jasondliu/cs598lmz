import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Now, the <code>m[:]</code> is empty even though I didn't unmap it. I had been under the impression that it would only be unmapped when it is garbage collected.
What I'd like to know is whether this is a bug in the standard library, or whether it is something I should expect. I've tried it on python 3.8.2 and 3.7.1.


A:

The documentation says that mmap is not a context manager, and its <code>__exit__</code> just does <code>close()</code>.
<blockquote>
<p>The optional size parameter specifies the size of the buffer. If omitted, the size defaults to the current size of the file. If larger than the file size, the file is extended with null bytes.</p>
<p>Note that file objects have an associated internal buffer which is flushed when the file object is closed. Therefore, if you open a file for updating and call mmap() with access=mmap.ACCESS_WRITE, any modifications you make to the data written via the mmap object will not be visible until the file object is closed.</p
