import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the error <code>ValueError: mmap length is zero</code> on the last line. This is on Ubuntu 16.04 with Python 3.5.2.
If I comment out the <code>f.truncate()</code> line, then the program runs without error.
Is this a bug in Python, or am I doing something wrong?


A:

<code>mmap.mmap</code> has a length parameter in its constructor. In your case, you are passing 0 as the length of the map. This is making <code>mmap</code> to raise a <code>ValueError</code> exception.
From the documentation:
<code>mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
</code>
<blockquote>
<p>Create a new memory-mapped file object. The length argument specifies the size of the buffer to be created. For a writeable buffer, the size cannot exceed the size of the file on disk. On Windows, the length argument is ignored, and the entire file is mapped.</p>

