import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
In Python 3.3, this code prints
<code>b'\x01'
</code>
In Python 3.5 and 3.6, this code prints
<code>b''
</code>
What happened?


A:

The documentation for <code>mmap</code>'s <code>truncate</code> method says:
<blockquote>
<p>If the current size is larger than the new size, the extra data is lost. If the current size is smaller than the new size, the file is extended with null bytes.</p>
</blockquote>
In Python 3.3, the <code>truncate</code> method didn't take into account the fact that the mmap object was still open, and so truncated the file.
In Python 3.5 and 3.6, the <code>truncate</code> method now takes into account that the mmap object is open for reading, and so it extends the file instead.
To fix this, you need to unmap the memory map before truncating:
<code>m.close()

