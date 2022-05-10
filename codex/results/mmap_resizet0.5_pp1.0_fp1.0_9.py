import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This will result in a <code>ValueError: mmap offset is greater than file size</code> exception.
I don't understand why the <code>mmap</code> object is not updated to reflect the truncation of the file.
I am using Python 3.8.1 on Windows 10.

