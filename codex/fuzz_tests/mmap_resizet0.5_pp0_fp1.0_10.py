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
It seems that <code>mmap</code> still thinks that the file is 1 byte long.
Is there a way to force <code>mmap</code> to update its view of the file size?


A:

Yes, you can use <code>mmap.resize</code> to resize the mmap.
<code>m.resize(0)
</code>

