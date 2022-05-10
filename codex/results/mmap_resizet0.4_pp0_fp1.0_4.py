import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The last line fails with <code>ValueError: mmap closed or invalid</code>.
I'm using Python 3.7.3 on Windows 10.
What am I doing wrong?


A:

The error is because you are trying to use the <code>mmap</code> object after you have closed it.
The <code>mmap</code> object is closed when you call <code>m.close()</code>.
The <code>mmap</code> object is invalidated when you call <code>f.truncate()</code>.
When you truncate the file, the <code>mmap</code> object is invalidated.  This means that the <code>mmap</code> object is no longer valid and cannot be used.
If you want to use the <code>mmap</code> object after truncating the file, you need to create a new <code>mmap</code> object.

