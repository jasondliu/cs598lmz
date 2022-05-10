import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: memory mapping closed or invalid</code>.
I would expect the <code>mmap</code> object to be updated when the file is truncated, but it seems that it's not the case.
Is there a way to get the <code>mmap</code> object to be updated when the file is truncated?


A:

The <code>mmap</code> object is not updated. You can use <code>m.resize(0)</code> to truncate it.

