import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I'm not sure why this is happening. The file is open in read/write mode, so I would expect the mmap to be able to read the bytes that were there before the truncate.
I'm using Python 3.6.1 on Windows 10.


A:

The problem is that the <code>mmap</code> object is not aware of the truncation.
You can fix it by calling <code>m.resize(0)</code> after the truncation.

