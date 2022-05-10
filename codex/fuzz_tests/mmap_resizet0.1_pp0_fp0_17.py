import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code works fine on Linux, but on Windows I get an exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I'm using Python 3.6.1 on Windows 10.
Is this a bug in Python or Windows?


A:

This is a bug in Python.
The problem is that the <code>mmap</code> object is not updated when the file is truncated.
The <code>mmap</code> object is updated when the file is resized, but not when it is truncated.
The <code>mmap</code> object is updated when the file is resized, but not when it is truncated.
The <code>mmap</code> object is updated when the file is resized, but not when it is truncated.
The <code>mmap</code> object is updated when the file is resized, but not when it is truncated.
The <code>mmap
