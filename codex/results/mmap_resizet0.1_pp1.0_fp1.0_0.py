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
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I'm not sure why this is happening. I'm using Python 3.6.1.


A:

The problem is that you're using <code>mmap.mmap</code> incorrectly. The second argument is the length of the mapping, not the size of the file.
<code>m = mmap.mmap(f.fileno(), 0)
</code>
should be
<code>m = mmap.mmap(f.fileno(), 1)
</code>

