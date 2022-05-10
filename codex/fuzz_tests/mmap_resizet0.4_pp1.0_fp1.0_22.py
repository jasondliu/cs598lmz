import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code prints <code>b'\x00'</code> instead of <code>b'\x01'</code>.
I think that the reason is that <code>mmap</code> doesn't update its size when the file is truncated.
Is there a way to force <code>mmap</code> to update its size?


A:

<blockquote>
<p>Is there a way to force mmap to update its size?</p>
</blockquote>
No, there isn't. You can't change the size of a memory-mapped file.
You can, however, create a new memory-mapped file, and copy the data from the old one to the new one.

