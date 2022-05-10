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
ValueError: cannot mmap an empty file
</code>
I don't understand why I get this error. I thought that the <code>mmap</code> object would be updated when I truncate the file.
I am using Python 3.6.1 on Windows 10.


A:

The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>The size argument specifies the initial size of the mapped region. If
  size is larger than the file, the file is extended to contain size
  bytes. If size is 0, the maximum length of the map will be the current
  size of the file, except that if the file is empty Windows raises an
  exception (you cannot create an empty mapping on Windows).</p>
</blockquote>
So, you can't create an empty mapping on Windows.

