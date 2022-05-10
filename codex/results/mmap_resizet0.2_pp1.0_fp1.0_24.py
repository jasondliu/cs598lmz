import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I think that the problem is that <code>mmap</code> doesn't know that the file has been truncated. Is there a way to tell <code>mmap</code> that the file has been truncated?
I'm using Python 3.4.3 on Windows 7.


A:

The problem is that the <code>mmap</code> object is not aware of the truncation.  You can fix this by calling <code>mmap.resize</code> after truncating the file.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:]
</code>

