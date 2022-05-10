import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I get an error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I'm using Python 3.6.1 on Windows 10.
How can I get the data from the file, even if it's empty?


A:

The problem is that <code>f.truncate()</code> doesn't change the length of the underlying file. It just sets the file position to the end of the file.
You can use <code>os.ftruncate</code> to truncate the file to a given length:
<code>import mmap
import os

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    os.ftruncate(f.fileno(), 0)
    a = m
