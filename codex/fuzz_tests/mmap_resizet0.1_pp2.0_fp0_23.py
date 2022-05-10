import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code> exception.
I understand that this is because the file is truncated and the offset is greater than the file size.
But I don't understand why the file is truncated.
I thought that the file size is not changed until the <code>mmap</code> object is closed.
Is this behavior correct?

