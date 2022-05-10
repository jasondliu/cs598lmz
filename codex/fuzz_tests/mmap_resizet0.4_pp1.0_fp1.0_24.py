import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I expected that <code>m[:]</code> would return <code>b''</code>.
I'm using Python 3.6.


A:

The documentation of <code>mmap</code> states:
<blockquote>
<p>The file size cannot be changed while the file is mapped.</p>
</blockquote>
So the behavior you are seeing is expected.

