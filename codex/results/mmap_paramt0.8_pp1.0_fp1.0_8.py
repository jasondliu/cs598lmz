import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, mmap.MAP_SHARED, mmap.PROT_WRITE)
    m[:] = bytes([1, 2, 3, 4, 5])
</code>
If I <code>cat</code> the file, it shows the 5 bytes as expected, but <code>ls -l</code> still says 1 byte. How do I update the size of the file?


A:

You can use the <code>os</code> module to adjust the size of the file:
<code>import os
os.resize('test', 5)
</code>

