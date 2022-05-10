import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code will print <code>b'\x00'</code> on Windows and <code>b'\x01'</code> on Linux.
I think that the problem is that the file is truncated before the <code>mmap</code> object is updated.
Is there a way to truncate a file and update the <code>mmap</code> object at the same time?


A:

You can use <code>mmap.resize</code> to resize the file and the <code>mmap</code> object at the same time.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    mmap.resize(m, 0)
    a = m[:]
    print(a)
</code>

