import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get <code>ValueError: mmap offset is greater than file size</code> on the last line.
I would expect the mmap to be updated to reflect the truncation.
Is there a way to make this work?

