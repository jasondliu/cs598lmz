import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read(1))
</code>
Output:
<code>b'\x00'
</code>
I was expecting to see <code>b'\x02'</code> instead. Why is this happening?


A:

According to the docs, the <code>length</code> argument of <code>mmap.mmap</code> is the size of the mapped memory.
<blockquote>
<p>The length argument specifies the <strong>size of the mapped memory</strong>.</p>
</blockquote>
So, you are mapping a memory of size 0, which is empty.

