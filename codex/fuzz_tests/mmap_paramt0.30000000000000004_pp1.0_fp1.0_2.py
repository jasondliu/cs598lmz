import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(0)
    m.close()
</code>
I get the error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m[0] = bytes(0)
TypeError: 'bytes' object does not support item assignment
</code>
I would expect the file to be modified, but it is not.
I am using Python 3.6.1 on Windows 10.


A:

You need to use <code>mmap.ACCESS_WRITE</code> flag when creating the <code>mmap</code> object. The default is <code>mmap.ACCESS_READ</code> which does not allow writing.
<code>m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
</code>

