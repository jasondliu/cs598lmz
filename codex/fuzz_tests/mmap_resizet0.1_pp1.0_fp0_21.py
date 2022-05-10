import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code prints <code>b'\x00'</code> instead of <code>b'\x01'</code>.
I know that I can use <code>mmap.resize</code> to resize the map, but I want to know why the map is not updated when the file is truncated.


A:

The <code>mmap</code> object is not updated when the file is truncated because the <code>mmap</code> object is not updated when the file is truncated.
The <code>mmap</code> object is a view of the file at a particular point in time. It does not update when the file changes.

