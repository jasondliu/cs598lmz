import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that the file is truncated, but I don't understand why the <code>mmap</code> object is not updated.
I'm using Python 3.6.5 on Windows 10.


A:

The <code>mmap</code> object is not updated because it is not supposed to be.
The <code>mmap</code> object is a view of the file, not a copy of the file.
If you want to update the file, you have to update the <code>mmap</code> object.

