import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that the file is truncated, but I don't understand why the <code>mmap</code> object is not updated.
I'm using Python 3.6.1 on Windows 10.


A:

The <code>mmap</code> object is not updated because it is not supposed to be updated.
The <code>mmap</code> object is a view of the file, not a copy of the file.  If you truncate the file, the <code>mmap</code> object is still a view of the file, but the file is now smaller.  The <code>mmap</code> object is not updated because it is not supposed to be updated.
If you want to truncate the file and update the <code>mmap</code> object, you can do this:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(0)
    a = m[:]
