import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I suppose that <code>m[:]</code> tries to read from the file, but the file has been truncated.
Is there any way to avoid this?


A:

The problem is that the <code>mmap</code> object is still pointing to the old file.
The way to fix it is to create a new <code>mmap</code> object after the truncation.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
</code>

