import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get the error:
<code>ValueError: mmap can't extend file to larger than 2GB on 32-bit system
</code>
How can I get the data from the mmap object?


A:

You can't.
The <code>mmap</code> object is a view into a file. If the file is truncated, the view is no longer valid.

