import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
<code>f.truncate()</code> throws the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    f.truncate()
ValueError: cannot truncate a mapped file
</code>
How is it possible that the file is still mapped, even though I've closed the <code>mmap</code> object?
Is there a way to truncate the file without closing and reopening it?

I'm using Python 3.6.4 on Windows 10.


A:

The problem is that <code>mmap</code> objects are not closed when their reference count reaches 0.
On POSIX systems, the <code>mmap</code> object has a <code>close()</code> method, which can be used to close the <code>mmap</code> object explicitly.
On Windows, the <code>mmap</code> object has a <code>close_fd()</code> method, which closes the file descriptor
