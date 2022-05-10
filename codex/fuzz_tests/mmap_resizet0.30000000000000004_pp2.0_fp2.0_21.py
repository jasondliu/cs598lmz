import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file was truncated and the mmap is now invalid, but why does the exception occur when I try to access the mmap?
I'm using Python 3.5.2 on Windows 10.


A:

The <code>mmap</code> object is not invalidated when the file is truncated. The <code>mmap</code> object is invalidated when you try to access it.
The <code>mmap</code> object is a wrapper around the <code>mmap</code> function in the C library. That function returns a pointer to the memory-mapped file, and that pointer is invalidated when the file is truncated.
The <code>mmap</code> object doesn't know that the file has been truncated, so it doesn't know that the pointer is invalid. It just tries to use the pointer,
