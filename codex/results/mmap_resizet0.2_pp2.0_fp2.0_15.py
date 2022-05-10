import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code will raise an exception:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
The problem is that <code>mmap</code> is not aware of the truncate operation.
Is there a way to make <code>mmap</code> aware of the truncate operation?
I'm using Python 3.7.3 on Windows 10.


A:

<code>mmap</code> is not aware of the truncate operation because it is not aware of the file at all.  It is a mapping of the underlying file descriptor, not the file.  The file descriptor is not aware of the truncate operation either.  The file descriptor is a handle to the underlying file object, not the file object itself.  The file object is not aware of the truncate operation either.  The file object is a wrapper around the underlying file descriptor, not the file descriptor itself.  The file object is not aware of the truncate operation either.  The file
