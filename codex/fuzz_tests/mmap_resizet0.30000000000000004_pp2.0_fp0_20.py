import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line throws <code>ValueError: mmap offset is greater than file size</code>.
I'm not sure if this is a bug or not. The documentation says:
<blockquote>
<p>If the file is resized, the size of the mmap will not change.</p>
</blockquote>
But it doesn't say what happens if the file is truncated.
I'm using Python 3.4.3 on Linux.

