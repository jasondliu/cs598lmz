import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expected the <code>a</code> variable to contain <code>b'\x00'</code>, but instead it is <code>b'\x01'</code>.
I was able to reproduce this in both Python 2.7 and Python 3.6.
Why is that?


A:

That's because the <code>mmap</code> object is not aware of the truncation. The <code>mmap</code> object is an abstraction of the underlying file, and the underlying file is not truncated until the <code>mmap</code> object is closed.
If you want to truncate the file and keep the <code>mmap</code> object open, you have to use the <code>resize</code> method:
<code>m.resize(0)
</code>

