import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file size is 0, and the offset is 1, but I don't understand why the offset is 1. I would expect it to be 0.
I'm using Python 3.5.1 on Windows 10.


A:

The problem is that you are using <code>mmap.mmap</code> incorrectly.
The first argument to <code>mmap.mmap</code> is the file descriptor, not the file object.
<code>m = mmap.mmap(f.fileno(), 0)
</code>
The second argument is the size of the mapping.
<code>m = mmap.mmap(f.fileno(), 0)
</code>
The third argument is the offset into the file.
<code>m = mmap.mmap(f.fileno(), 0, 0)

