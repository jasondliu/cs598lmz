import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x01'</code>
But if I change the line <code>f.truncate()</code> to <code>m.resize(0)</code> the output is <code>b''</code>
Why is that?


A:

The <code>mmap</code> object is a view into the underlying file.  When you truncate the file, the view is still there, but the data is gone.  When you resize the mmap, the view is gone, and the data is gone.

