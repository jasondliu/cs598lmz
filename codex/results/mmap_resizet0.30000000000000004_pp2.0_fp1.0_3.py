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
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I think it's because <code>truncate</code> doesn't change the file size immediately, but only after the file is closed.
Is there a way to change the file size immediately?
I'm using Python 3.5.2.


A:

You can use <code>os.ftruncate</code> to truncate the file immediately:
<code>import mmap
import os

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    os.ftruncate(f.fileno(), 0)
    a = m[:]
</code>

