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
I know that I can use <code>mmap.resize</code> to resize the mmap object, but I can't find a way to resize the underlying file.
Is there a way to resize the underlying file?


A:

You can use <code>os.ftruncate</code> to truncate the file.
<code>import mmap
import os

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    os.ftruncate(f.fileno(), 0)
    a = m[:]
    print(a)
</code>

