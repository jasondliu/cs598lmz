import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line gives <code>IOError: [Errno 22] Invalid argument</code>
It seems like python can't handle truncating and mmap at the same time. Is there a way to do so?
Note: This is just an example. 


A:

The error is reproduceable both with Python 2.7.11 and Python 3.6.2 on both Linux and Windows.
On Linux, it appears to be caused by Python using the <code>ftruncate()</code> method to truncate the file. If a file is mapped, then all views of the map must be unmapped, except the single part that is to be truncated:
<blockquote>
<p><strong>EINVAL</strong>  size is negative</p>
<p><strong>EINVAL</strong>  the least significant bit of flags is nonzero and <code>&lt;code&gt;addr&lt;/code&gt;</code> is not an address returned by <code>&lt;code&gt;mmap()&lt;/code&gt;</code>; or <code
