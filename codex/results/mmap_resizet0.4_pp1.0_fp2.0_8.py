import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line throws a <code>ValueError: mmap offset is greater than file size</code>.
I don't understand why this happens. I thought that the <code>mmap</code> object would be able to access the file contents until the file is closed.
I'm using Python 3.8.2 on Windows 10.


A:

The problem is that the <code>mmap</code> object is not updated when you truncate the file. You can see this by printing out the length of the <code>mmap</code> object before and after truncation:
<code>&gt;&gt;&gt; with open('test', 'r+b') as f:
...     m = mmap.mmap(f.fileno(), 0)
...     print(len(m))
...     f.truncate()
...     print(len(m))
...
1
1
</code>
When you access the <code>mmap</code> object after truncation, it tries to access memory that is no longer mapped to the file.
You can work around this by calling <code
