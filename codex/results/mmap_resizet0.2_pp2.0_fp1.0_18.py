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
ValueError: cannot read from closed file
</code>
I'm not sure why this is happening. I thought that the <code>mmap</code> object would keep the file open.
I'm using Python 3.6.5 on Ubuntu 18.04.


A:

The problem is that <code>mmap</code> objects are tied to the file descriptor, not the file object. When you truncate the file, the file descriptor is closed, and the <code>mmap</code> object is no longer valid.
You can get around this by using <code>os.dup</code> to duplicate the file descriptor before truncating the file:
<code>import mmap
import os

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    fd =
