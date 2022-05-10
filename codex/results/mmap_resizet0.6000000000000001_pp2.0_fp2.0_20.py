import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # segfault here
</code>
How can I get the content of the file after <code>f.truncate()</code>?


A:

The <code>mmap</code> module has a <code>resize</code> method to adjust the mapping to the file size:
<code>m.resize(0)
</code>
The <code>mmap</code> module also has a <code>close</code> method to remove the mapping on the file:
<code>m.close()
</code>

