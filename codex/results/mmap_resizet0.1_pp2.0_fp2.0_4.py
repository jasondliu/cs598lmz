import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that the file is truncated and the mmap is no longer valid.
But I don't understand why the mmap is still trying to read from the file.
I would expect that the mmap is invalidated and the <code>m[:]</code> line would raise an exception.
Is there a way to make the mmap invalidated when the file is truncated?

