import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I would expect the <code>mmap</code> object to be updated with the new file size.
Is there a way to make it work?


A:

<code>mmap</code> is not updated when the file is truncated.
You can use <code>mmap.resize</code> to resize the <code>mmap</code> object:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(f.tell())
    a = m[:]
</code>

