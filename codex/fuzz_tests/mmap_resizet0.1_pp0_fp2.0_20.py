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
I'm not sure why this is happening. I'm using Python 3.6.1 on Windows 10.


A:

The problem is that you're using <code>mmap.mmap</code> with a length of 0. This means that the mmap object is empty, and so trying to access it will fail.
If you want to use <code>mmap.mmap</code> with a length of 0, you need to use the <code>access</code> parameter to specify that you want to be able to read from the mmap object.
<code>m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
</code>
However, if you want to be able to read and write to the mmap object, you should use the <code>mmap.MAP_SHAR
