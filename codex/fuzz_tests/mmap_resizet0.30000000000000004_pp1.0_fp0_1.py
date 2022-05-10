import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line throws <code>ValueError: mmap offset is greater than file size</code>.
I would like to know what is the correct way to truncate the file and keep the mmap valid.
I am using Python 3.5.2 on Windows 10.


A:

The problem is that the <code>mmap</code> object is still pointing to the old file size.
You can use <code>mmap.resize</code> to resize the <code>mmap</code> object:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:]
</code>

