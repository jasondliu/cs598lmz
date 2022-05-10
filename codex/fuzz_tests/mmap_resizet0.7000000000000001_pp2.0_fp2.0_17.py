import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

# This fails with ValueError: mmap offset is greater than file size
#m[0] = bytes('a', 'utf-8')

# This fails with ValueError: mmap closed or invalid
#m.close()
</code>
I don't know if these bugs are related, but I can't help but notice how similar they are.

