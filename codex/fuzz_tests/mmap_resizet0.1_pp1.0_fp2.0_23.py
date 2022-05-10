import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file size is 0, but I don't understand why the mmap offset is greater than the file size.
I'm using Python 3.6.5 on Windows 10.


A:

The problem is that the <code>mmap</code> object is still pointing to the old file size.
The documentation for <code>mmap</code> says:
<blockquote>
<p>The size argument specifies the initial size of the mapped region. If
  size is larger than the file, the file is extended to contain size
  bytes. If size is 0, the maximum length of the map will be the current
  size of the file, except that if the file is empty Windows raises an
  exception (you cannot create an empty mapping on Windows).</p>
</blockquote>
So, if you
