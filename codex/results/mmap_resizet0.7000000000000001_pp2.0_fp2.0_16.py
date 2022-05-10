import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This produces a <code>ValueError: mmap offset is greater than file size</code>. 
Is there another way to read the file?


A:

The file is truncated before the <code>mmap</code> is created, so the offset is no longer valid. Try this:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    f.truncate()
</code>

