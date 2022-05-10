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
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I'm not sure why this is happening. I'm on Windows 10 and Python 3.6.


A:

The problem is that you are using <code>mmap.mmap</code> with a length of 0. This means that the mmap object is not actually mapped to anything.
If you change the length to 1, it works:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    f.truncate()
    a = m[:]
</code>

