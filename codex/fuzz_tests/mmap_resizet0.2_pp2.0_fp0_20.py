import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code> exception.
I know that I can use <code>mmap.resize</code> to resize the mmap object, but I want to know why this exception is raised.
I think that the mmap object should be resized automatically when the file is truncated.
Is this a bug?

