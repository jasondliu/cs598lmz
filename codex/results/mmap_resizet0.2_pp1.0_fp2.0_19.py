import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I know that I can use <code>mmap.resize</code> to resize the mmap, but I don't want to do that. I want to know why the mmap is not updated when the file is truncated.


A:

The <code>mmap</code> object is not updated when the file is truncated because the <code>mmap</code> object is not updated when the file is truncated.
The <code>mmap</code> object is a snapshot of the file at the time it was created.  It is not updated when the file is changed.  If you want to see the changes, you have to create a new <code>mmap</code> object.

