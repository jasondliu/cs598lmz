import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
But it seems that <code>m[:]</code> is not actually reading the file but the mmap buffer.
Is there a way to read the file after the truncate without closing the mmap?

