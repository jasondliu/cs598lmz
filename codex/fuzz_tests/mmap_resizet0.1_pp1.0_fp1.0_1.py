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
I'm not sure why this is happening. I'm using Python 3.6.5 on Windows 10.


A:

The problem is that the <code>mmap</code> object is still pointing to the old file size.
You can fix this by calling <code>m.resize(0)</code> after truncating the file.

