import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file has been truncated, but I don't understand why the mmap object is still referencing the old file size.
I'm using Python 3.6.3 on Linux.


A:

The <code>mmap</code> object is not referencing the old file size. It is referencing the old file contents.
The <code>mmap</code> object is a view of the file contents. The file contents are not the same as the file size.
When you truncate the file, the file size is changed, but the file contents are not. The file contents are still the same as before.
The <code>mmap</code> object is a view of the file contents. The file contents are not the same as the file size.

