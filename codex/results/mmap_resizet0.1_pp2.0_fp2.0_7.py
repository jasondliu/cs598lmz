import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I would expect that the <code>mmap</code> object would be updated to reflect the truncation.
Is there a way to do this?


A:

The <code>mmap</code> object is not updated to reflect the truncation.
The <code>mmap</code> object is a view of the file at the time it was created.
The <code>mmap</code> object is not updated to reflect changes to the file.
The <code>mmap</code> object is not updated to reflect changes to the file descriptor.
The <code>mmap</code> object is not updated to reflect changes to the file descriptor's file.
The <code>mmap</code> object is not updated to reflect changes to the file descriptor's file's size.
The <code>mmap</code> object is not updated to reflect changes to the file descriptor's file's contents.
The <code>mmap</code> object is not updated to reflect changes to the file descriptor's file's contents at the time the
