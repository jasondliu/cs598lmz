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
Why does this happen? I thought that the file was truncated and the mmap should be updated.


A:

The <code>mmap</code> object is not updated.  You need to call <code>mmap.resize</code> to resize the mmap object.

