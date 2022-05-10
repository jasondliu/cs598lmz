import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = bytes(2) # modify the file
</code>
The code above opens a file, write one byte (1), then tries to overwrite it.
I get the error <code>Buffer size must be a multiple of element size</code>
I tried <code>m.resize(1)</code> and <code>m.resize(1, 0)</code> but both return <code>ValueError: cannot resize a read-only memory map</code>.
Is it possible to do this in one step?


A:

I think you need to use the <code>os.open</code> function to obtain a file descriptor, and then <code>mmap.mmap</code> to create a memory map.
<code>import os
import mmap

with os.open('test', os.O_RDWR) as fd:
    m = mmap.mmap(fd, 1)
    m[:] = bytes(2)
</code>

