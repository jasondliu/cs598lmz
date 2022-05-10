import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises a <code>ValueError</code> with the message <code>mmap offset is greater than file size</code>.
I would expect the <code>mmap</code> object to be updated to reflect the new file size.
Is this a bug or am I doing something wrong?

