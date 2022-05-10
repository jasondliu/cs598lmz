import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This code raises an exception <code>ValueError: mmap offset is greater than file size</code>. I understand that the file has been truncated, so the mmap is now invalid. But why doesn't the mmap size get updated?
<code>m.size()</code> still returns 1, even after the truncation.

