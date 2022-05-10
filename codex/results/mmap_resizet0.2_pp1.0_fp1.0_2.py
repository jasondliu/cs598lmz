import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x00'</code> instead of <code>b'\x01'</code>.
I'm using Python 3.5.2 on Windows 7.


A:

The problem is that the <code>mmap</code> object is still pointing to the old file.
You can fix this by calling <code>m.close()</code> before truncating the file.

