import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 1
</code>


A:

You need to actually resize the file (<code>truncate</code> skips any existing data, but when no data exists, the file has 0 bytes). You can use the <code>resize()</code> method:
<code>m = mmap.mmap(f.fileno(), 0)
m.resize(128)  # make file 128-bytes in size
</code>

