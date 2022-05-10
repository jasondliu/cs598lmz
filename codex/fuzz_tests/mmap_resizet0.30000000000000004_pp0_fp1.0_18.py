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
I'm not sure why this is happening. I'm using Python 3.3.3 on Windows 7.


A:

The problem is that the file size has changed, but the mmap object still thinks it's the same size.
You can use <code>m.resize(0)</code> to fix it.

