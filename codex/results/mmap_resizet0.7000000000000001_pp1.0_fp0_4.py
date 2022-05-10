import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This gives a <code>ValueError: mmap offset is greater than file size</code>
Is there a way to get the bytes in the memory map before it is resized?
EDIT
I do not want to close the file. I am looking for a way to get the bytes in the memory map before the file is resized.


A:

The problem is that <code>truncate</code> does not resize the file in place, but moves the file pointer to the end. The memory map is therefore pointing to a non-existent part of the file.
You can use <code>posix_fallocate</code> instead:
<code>import mmap, os
from mmap import PAGESIZE, MAP_PRIVATE
from os import posix_fallocate
from os import O_RDWR

with open('test', 'wb') as f:
    f.write(bytes(1))

f = os.open('test', O_RDWR)

posix_fallocate(f, 0, PAGESIZE)

m = mmap.mmap(
