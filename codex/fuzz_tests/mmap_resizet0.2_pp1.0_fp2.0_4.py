import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I know that I can use <code>mmap.resize</code> to fix this, but I want to know why this error is raised.
I think that the error is raised because the file size is changed, but the mmap object is not updated.
Is my guess correct?


A:

The error is raised because the mmap object is not updated.
The mmap object is not updated because the file size is changed.
The file size is changed because the mmap object is not updated.

