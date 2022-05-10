import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # crashes
</code>
On Linux:
<code>$ python ./test.py
Traceback (most recent call last):
  File "./test.py", line 10, in &lt;module&gt;
    a = m[:] # crashes
ValueError: cannot truncate a mapped object
</code>
On Windows, it just crashes with a segfault (in the Python interpreter's executable).
Is this a bug? Or did I miss something here?
The same code works with Python 2, so it's possible it's a bug in the Python 3 port of the mmap module.


A:

From the docs:
<blockquote>
<p>The mmap module provides a way of mapping files into memory. This is
  especially useful for applications that need to treat files as random
  access arrays of data. The mmap object behaves like a file (it has a
  fileno method) and a ctypes array, with some restrictions. <strong>Changes to
  mmap objects do not appear in the underlying file until the <em>flush</em>()
  or <strong><em>close</em></
