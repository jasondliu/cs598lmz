import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>. I understand that the mmap is not aware of the truncation, but how can I make it aware?


A:

The <code>mmap</code> module is not aware of truncation, but the <code>mmap</code> object itself is, as it has a <code>resize()</code> method.
<code>m.resize(0)
a = m[:]
</code>

