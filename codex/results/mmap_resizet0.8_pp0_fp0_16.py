import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I know that this code does not make sense, but I want to understand what happens. I thought that for <code>f.truncate</code> mmap would try to map the <code>[:]</code> from the file, but it does not. Why?


A:

From the documentation of <code>mmap.mmap</code>:
<blockquote>
<p>mmap.mmap(fileno, length[, access[, offset]])</p>
<p>Maps length bytes from the file specified by the file descriptor fileno, <strong>and returns a mmap object</strong>. If length is larger than the current size of the file, the file is extended to contain length bytes.</p>
</blockquote>
Your call to mmap creates a mapping of the contents of the file, not of the file itself, thus the mapping is not updated when the file is truncated.
Note that you are reading the contents of the mapping, so it's memory, not the file, that you are reading.

