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
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file size is 0, but I don't understand why the offset is greater than the file size.
I'm using Python 3.6.5 on Windows 10.


A:

The problem is that you are using <code>f.fileno()</code> to get the file descriptor.  This is not a good idea, because the file descriptor is not guaranteed to be the same after a <code>truncate</code> call.  From the documentation:
<blockquote>
<p>The file descriptor is not guaranteed to be valid after the file is closed (whether it is closed explicitly, or by garbage collection).</p>
</blockquote>
If you use <code>f.fileno()</code> to get the file descriptor, then you are not guaranteed to get the same file descriptor after the <code>truncate</
