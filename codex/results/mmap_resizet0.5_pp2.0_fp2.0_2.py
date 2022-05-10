import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
How can I read a file that is being truncated, and how can I truncate a file that is being read?


A:

The <code>mmap</code> object does not know about the file size change. You need to tell it about it:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
</code>
Note that this will only work if the file is opened in <code>r+</code> mode, not <code>r</code> mode.

