import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line throws <code>ValueError: mmap closed or invalid</code>. Why? In my understanding, even though the file has been truncated, the mmap object should still be valid. The same error does not occur for <code>m[0]</code>.


A:

The documentation (at least in the Python 2 version I'm looking at) says:
<blockquote>
<p>In order to retain the refcount semantics of Python file objects, the mmap object should be the only object holding a reference to the file object. Once the mmap object is closed, or destroyed by garbage collection, the underlying file may be closed if it was opened by mmap.</p>
</blockquote>
The file was opened in append mode, which means that the only way to close it is to close the mmap object.

