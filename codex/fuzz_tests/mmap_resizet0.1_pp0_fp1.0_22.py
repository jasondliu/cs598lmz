import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This code raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file size is 0, but why does the mmap object still exist?
I'm using Python 3.4.3 on Windows 7.


A:

The <code>mmap</code> object is still there because you haven't closed it.
You can't use the <code>with</code> statement to close the <code>mmap</code> object, because it's not the context manager.  The context manager is the file object.
You can use <code>mmap.mmap.close</code> to close the <code>mmap</code> object.

