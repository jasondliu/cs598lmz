import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that the file size is 0, but I don't understand why the offset is greater than the file size.
I'm using Python 3.6.1 on Windows 10.


A:

The problem is that you are using the <code>mmap</code> module incorrectly. The <code>mmap</code> module is used to map a file into memory. The <code>mmap</code> object is a view of the file. If you truncate the file, the <code>mmap</code> object is no longer valid.
If you want to truncate the file, you need to unmap the file first.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.close()
    f.truncate()
</code>

