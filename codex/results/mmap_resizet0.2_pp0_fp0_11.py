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


A:

The problem is that the <code>mmap</code> object is still pointing to the old file size, which is 1 byte.  When you truncate the file, the file size is now 0 bytes.  So when you try to access the <code>mmap</code> object, it tries to access a byte that doesn't exist.
The solution is to resize the <code>mmap</code> object to the new file size.  You can do this by calling <code>mmap.resize</code>.  For example:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fil
