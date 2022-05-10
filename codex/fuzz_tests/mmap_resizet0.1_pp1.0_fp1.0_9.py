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
I'm not sure why this is happening. I'm using Python 3.6.1 on Windows 10.


A:

The problem is that you're using <code>mmap.mmap</code> with a length of 0. This means that the mmap object will have a length of 0, and so any attempt to access it will fail.
You need to use a length of 1, or use <code>mmap.mmap.size()</code> to get the size of the file.

