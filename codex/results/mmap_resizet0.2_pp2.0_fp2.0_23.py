import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I am using Python 3.4.3 on Windows 7.
Is there a way to get the contents of the file after truncating it?


A:

This is a bug in the Windows implementation of <code>mmap</code>.
The bug is that the <code>mmap</code> object is not updated when the file is truncated.
The bug is fixed in Python 3.5 and 3.6.

