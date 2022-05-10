import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
<code>a</code> is <code>b'\x00'</code> instead of <code>b'\x01'</code>.
I don't understand what's going on here.
I thought that the <code>mmap</code> object was a view on the file.
I thought that the <code>mmap</code> object was not affected by the <code>truncate</code> call.
I thought that the <code>mmap</code> object was not affected by the <code>close</code> call.
I thought that the <code>mmap</code> object was not affected by the <code>open</code> call.
I thought that the <code>mmap</code> object was not affected by the <code>write</code> call.
I thought that the <code>mmap</code> object was not affected by the <code>read</code> call.
I thought that the <code>mmap</code> object was not affected by the <code>seek</code> call.
I thought that the <code>mmap</code> object was
