import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that <code>mmap</code> is a view of the file, and that the file is truncated, but I don't understand why the <code>mmap</code> is not updated.
Is there a way to update the <code>mmap</code> after truncating the file?


A:

The <code>mmap</code> object is not updated because it is not supposed to be updated.
The <code>mmap</code> object is a view of the file, and the file is truncated.
The <code>mmap</code> object is not updated because it is not supposed to be updated.
The <code>mmap</code> object is a view of the file, and the file is truncated.
The <code>mmap</code> object is not updated because it is not supposed to be updated.
The <code>mmap</code> object is a view of the file, and the file is truncated.
The <code>mmap</code> object is not updated
