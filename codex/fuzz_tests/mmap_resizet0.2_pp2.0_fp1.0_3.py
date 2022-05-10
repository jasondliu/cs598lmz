import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that the file is truncated, but I don't understand why the mmap object is not updated.
I'm using Python 3.5.2.


A:

The <code>mmap</code> object is not updated because the file is truncated. The <code>mmap</code> object is a view of the file, and the file is truncated.
The <code>mmap</code> object is not updated because the file is truncated. The <code>mmap</code> object is a view of the file, and the file is truncated.
The <code>mmap</code> object is not updated because the file is truncated. The <code>mmap</code> object is a view of the file, and the file is truncated.
The <code>mmap</code> object is not updated because the file is truncated. The <code>mmap</code> object is a view of the file, and the file is truncated.
The <code
