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
I can see that the file is truncated, but the mmap object still thinks it's the same size.  Is there a way to get the mmap object to update its size?


A:

You can use <code>m.resize(new_size)</code> to resize the mmap object.

