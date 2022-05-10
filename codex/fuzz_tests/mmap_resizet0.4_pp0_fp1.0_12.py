import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises <code>ValueError: mmap offset is greater than file size</code>.
I can't find any mention of this in the documentation. Is this expected behavior? Is there a way to achieve what I'm trying to do?

