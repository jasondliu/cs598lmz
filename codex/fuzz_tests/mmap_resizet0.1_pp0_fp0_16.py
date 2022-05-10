import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file size is 0, but I don't understand why the offset is greater than the file size.
I'm using Python 3.6.5 on Windows 10.


A:

The problem is that you're using <code>mmap.mmap</code> incorrectly.
The first argument to <code>mmap.mmap</code> is the file descriptor, not the file object.  The second argument is the length of the mapping.  You're passing <code>0</code> as the length, which means that the mapping will be the length of the file.  But the file is empty, so the mapping is empty.
You can fix this by passing <code>-1</code> as the length, which means that the mapping will be the length of the file.  But the file is empty, so the
