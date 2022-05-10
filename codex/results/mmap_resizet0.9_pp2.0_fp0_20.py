import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This example fails with
<code>Traceback (most recent call last):
  File "tmp.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
How to mmap a file and remove file contents at the same time?


A:

<code>f.truncate(0)</code> resets the length of the file. It does not resize the map.
Call <code>mmap.resize()</code> after calling <code>truncate()</code>:
<code>m.resize(0)
</code>
This is quite a bit more transparent than trying to remove the file behind the map's back by truncating the file descriptor; you should use the <code>mmap</code> API directly to change the mapping's size.

