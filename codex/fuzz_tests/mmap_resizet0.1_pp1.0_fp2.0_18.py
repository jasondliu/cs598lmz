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
I understand that the mmap is pointing to the old file size, but I don't know how to fix it.


A:

You can't use <code>mmap</code> to map a file that has been truncated.  The <code>mmap</code> object is tied to the file descriptor, and the file descriptor is tied to the file size.  You can't change the file size without closing the file descriptor.
If you want to truncate the file, you have to close the <code>mmap</code> object first.

