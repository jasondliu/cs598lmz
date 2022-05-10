import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that the file size is 0 after the <code>truncate</code> call, but I don't understand why the <code>mmap</code> object is not updated.
Is there a way to update the <code>mmap</code> object after a <code>truncate</code> call?


A:

The <code>mmap</code> object is not updated because it is not supposed to be updated.
The <code>mmap</code> object is a view of the file at a given point in time. It is not a view of the file descriptor.
If you want to update the <code>mmap</code> object, you need to close it and reopen it.

