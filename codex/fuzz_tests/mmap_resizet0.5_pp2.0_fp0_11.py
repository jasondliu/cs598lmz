import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This gives me a <code>ValueError: mmap closed or invalid</code> when I try to access the <code>mmap</code> object.
How can I prevent that error?
I'm using Python 3.7.2 on Linux 4.17.7-1-ARCH.


A:

From the docs:
<blockquote>
<p>If the file is resized or otherwise modified in a way that affects its size, mmap() must be called again on the same file object to reflect the changes in the map.</p>
</blockquote>
So you need to re-create the <code>mmap</code> object after you've truncated the file.

