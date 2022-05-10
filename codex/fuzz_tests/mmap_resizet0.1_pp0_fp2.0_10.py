import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I know that <code>mmap</code> is not a good solution for this problem, but I want to know why this error is raised.
I think that <code>mmap</code> should be able to read the file even if it is truncated.

