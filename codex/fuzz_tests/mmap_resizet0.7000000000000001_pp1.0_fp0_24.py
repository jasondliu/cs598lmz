import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises an <code>ValueError: mmap offset is greater than file size</code>.  It seems that <code>mmap</code> is still bound to the old file size, is there a way to force it to update?


A:

mmap seems to be bound to the file size, so it is not possible to do what you want.
But you can use <code>m.resize()</code> to resize the mapped area to the new file size.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(f.tell())
    a = m[:]
</code>

