import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code fails with <code>ValueError: mmap offset is greater than file size</code> on the last line.
I understand why this happens (the file is empty, so the offset is out of bounds), but I don't know how to fix it.
The reason I'm doing this is because I'm using <code>mmap</code> to read a file, and I want to truncate the file while I'm reading it.


A:

You can use <code>mmap.resize()</code> to resize the <code>mmap</code> object.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(0)
    a = m[:]
</code>

