import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I would like to know why this error is raised.
I am using Python 3.6.5 on Windows 10.


A:

The problem is that you are using <code>mmap.mmap</code> with a size of 0. This means that the mmap object is empty, and thus any attempt to access it will fail.
The solution is to use <code>mmap.mmap</code> with a size of 1, or to use <code>mmap.mmap</code> with a size of 0 and then use <code>mmap.resize</code> to resize the mmap object to 1.

