import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
    m.close()
</code>
It works fine, but when I try to do the same with <code>mmap.PROT_READ</code> protection, it fails with <code>mmap.error: [Errno 1] Operation not permitted</code>:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
    m[0] = bytes(2)
    m.close()
</code>
What is the reason of this? Is it possible to write to memory-mapped file opened with <code>mmap.PROT_READ</code>?


A:

<blockquote>
<p>Is it possible to write to memory-mapped file opened with mmap.PROT_READ?</p>
</blockquote>
No, it isn't.  The <code>
