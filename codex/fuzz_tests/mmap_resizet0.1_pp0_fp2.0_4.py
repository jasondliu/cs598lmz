import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I would expect the <code>mmap</code> object to be updated when the file is truncated.
Is there a way to make this work?


A:

The <code>mmap</code> object is not updated when the file is truncated.
The <code>mmap</code> object is a view of the file, and the file is truncated.
The <code>mmap</code> object is not updated when the file is truncated.
The <code>mmap</code> object is a view of the file, and the file is truncated.
The <code>mmap</code> object is not updated when the file is truncated.
The <code>mmap</code> object is a view of the file, and the file is truncated.
The <code>mmap</code> object is not updated when the file is truncated.
The <code>mmap</code> object is a view of the file, and the file is truncated.
The <code>mmap
