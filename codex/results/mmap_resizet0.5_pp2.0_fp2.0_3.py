import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()

with open('test', 'rb') as f:
    a = f.read()
</code>
The last line fails with <code>ValueError: I/O operation on closed file</code>.
I can see that the mmap object is closed, but I don't understand why.
I am using Python 3.4.3


A:

<code>mmap</code> objects are designed to work with the file in the state it was at the time the <code>mmap</code> was created.  In particular, they do not update as the file size changes.  If you want to use <code>mmap</code> to access the new file contents, you need to create a new <code>mmap</code> object.

