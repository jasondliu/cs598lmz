import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code> on the last line.
I'm using Python 3.6.3 on Windows 10.
I'm not sure if this is a bug or if I'm doing something wrong.

