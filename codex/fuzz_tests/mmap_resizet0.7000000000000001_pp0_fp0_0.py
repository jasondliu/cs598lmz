import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
My expected result is that <code>a == bytes(1)</code>, but my actual result is <code>a == bytes()</code>.
It seems that truncating the file modifies the mapping. Is there a way to truncate a file without modifying the mapping, or a way to update the mapping so that the old contents are still accessible?

