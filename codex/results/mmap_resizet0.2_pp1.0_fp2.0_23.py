import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code fails with <code>ValueError: mmap offset is greater than file size</code>.
I understand that the file is truncated, but I don't understand why the <code>mmap</code> object is not updated.
Is there a way to update the <code>mmap</code> object?

