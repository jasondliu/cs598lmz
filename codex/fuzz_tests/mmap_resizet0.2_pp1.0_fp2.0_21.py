import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I would expect that the <code>mmap</code> object would be updated to reflect the truncation, but it seems that it isn't.
Is there a way to make the <code>mmap</code> object aware of the truncation?


A:

The <code>mmap</code> object is not aware of the truncation because it is not aware of the file.  The <code>mmap</code> object is a view of the file, but it is not the file.  The <code>mmap</code> object is not updated because the file is not updated.  The file is not updated because the file is not open.  The file is not open because you closed it.
The <code>mmap</code> object is a view of the file, but it is not the file.  The <code>mmap</code> object is not updated because the file is not updated.  The file is not updated because the file is not open.  The file is not open because you closed it.
The <
