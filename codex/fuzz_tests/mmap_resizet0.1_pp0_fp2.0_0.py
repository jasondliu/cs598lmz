import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I think it's because <code>mmap</code> doesn't know that file size is changed.
How can I fix this?


A:

You can't.
The <code>mmap</code> object is a view into the file, and the file is truncated.
You can't have a view into a file that doesn't exist.

