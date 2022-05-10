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
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file size is 0, but I don't understand why the offset is greater than the file size.
I'm using Python 3.6.5 on Windows 10.


A:

The problem is that you're using <code>f.fileno()</code> to get the file descriptor, and then you're truncating the file.  The file descriptor is still open, but the file has been truncated, so the offset is now greater than the file size.
You can fix this by using <code>f.truncate(0)</code> instead of <code>f.truncate()</code>.  This will truncate the file to zero bytes, but it won't close the file descriptor.

