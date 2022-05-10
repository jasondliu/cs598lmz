import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I know that I can use <code>mmap.resize</code> to change the size of the mapping, but I don't know how to get the new size of the file.
Is there a way to get the new size of the file after <code>truncate</code>?


A:

You can use <code>os.stat</code> to get the new size of the file.
<code>import mmap
import os

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:os.stat('test').st_size]
</code>

