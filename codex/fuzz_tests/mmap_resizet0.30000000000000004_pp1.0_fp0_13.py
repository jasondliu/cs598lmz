import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line throws <code>ValueError: mmap offset is greater than file size</code>.
I can't find anything in the documentation about this. Is it a bug or am I doing something wrong?


A:

The file is truncated to size 0, so the offset is greater than the file size.

