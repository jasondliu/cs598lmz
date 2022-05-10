import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises <code>ValueError: mmap offset is greater than file size</code>.
I'm not sure if this is a bug or if I'm missing something.
I'm using Python 3.6.5 on Windows 10.


A:

The <code>mmap</code> module is not meant to be used with a file that is being truncated.
The <code>mmap</code> module is meant to be used with a file that is not being truncated.
If you want to truncate a file, you should use the <code>truncate</code> method of the file object.

