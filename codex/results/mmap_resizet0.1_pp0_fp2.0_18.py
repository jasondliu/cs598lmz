import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code will raise an exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I know that I can use <code>m.resize(0)</code> to fix this, but I want to know why <code>f.truncate()</code> doesn't work.
I'm using Python 3.6.


A:

The <code>mmap</code> object is not aware of the truncation. It still thinks the file is the same size as it was when the <code>mmap</code> was created.
The <code>mmap</code> object is a wrapper around a memory-mapped file. The file is mapped into memory, and the <code>mmap</code> object is a view into that memory.
The <code>mmap</code> object is not aware of the file. It doesn't know that the file has been truncated. It doesn't know that the file has been
