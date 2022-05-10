import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0
    m.close()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    m[0] = 0
TypeError: 'mmap.mmap' object does not support item assignment
</code>
I am using Python 3.6.3 on Windows 10.
How can I fix this?


A:

The <code>mmap</code> object is read-only by default. You need to pass the <code>access</code> parameter to <code>mmap.mmap</code> to allow writing:
<code>m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
</code>

