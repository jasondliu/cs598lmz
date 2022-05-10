import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the mmap is pointing to a file that is now empty, but I don't understand why the mmap is not updated when the file is truncated.
I'm using Python 3.6.5 on Windows 10.


A:

The <code>mmap</code> object is not updated when the file is truncated because it is not supposed to be.
The <code>mmap</code> object is a view of the file, not a view of the file descriptor.
The file descriptor is a handle to the file, not the file itself.
When you truncate the file, you are changing the file, not the file descriptor.
The <code>mmap</code> object is a view of the file, not the file descriptor.
The <code>mmap</code> object is not updated when you trunc
