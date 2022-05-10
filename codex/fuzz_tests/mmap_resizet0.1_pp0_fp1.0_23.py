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
I understand that the file size is 0, but I don't understand why the offset is greater than the file size.
I'm using Python 3.6.1 on Windows 10.


A:

The problem is that you are using <code>mmap.mmap</code> with a file size of 0.
<code>mmap.mmap(f.fileno(), 0)
</code>
This is not allowed. From the documentation:
<blockquote>
<p>The size argument specifies the size of the buffer used to hold the
  mapped data. If size is larger than the current size of the file, the
  file is extended to contain size bytes. If size is 0, the maximum size
  of the map is the current size of the file, except that if the file is
  empty Windows raises an exception (you cannot create an
