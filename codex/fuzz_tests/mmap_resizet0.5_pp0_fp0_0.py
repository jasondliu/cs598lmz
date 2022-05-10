import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises an exception: <code>mmap.error: [Errno 9] Bad file descriptor</code>.
I'm using Python 3.4.2 on Windows.


A:

The documentation for <code>mmap</code> states that:
<blockquote>
<p>The file must remain open for the lifetime of the mmap object, but may be closed after the mmap object is finalized.</p>
</blockquote>
So, you should close the file after you've created the <code>mmap</code> object, but before you try to access it.

