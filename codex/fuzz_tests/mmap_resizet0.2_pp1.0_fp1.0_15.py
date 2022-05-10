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
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I am using Python 3.6.1 on Windows 10.
I have tried to use <code>mmap.ACCESS_READ</code> and <code>mmap.ACCESS_WRITE</code> but it didn't help.
Is there a way to truncate a file while keeping the mmap object valid?


A:

You can't do that. The mmap object is a view into the file, and the file has changed.

