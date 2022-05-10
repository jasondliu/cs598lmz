import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.close()
</code>
This is the error I get:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m[0] = b'\x00'
TypeError: 'mmap.mmap' object does not support item assignment
</code>
I'm using Python 3.5.2 on Windows 10.


A:

The <code>mmap</code> object is read-only by default. You need to set the <code>access</code> parameter to <code>mmap.ACCESS_WRITE</code> to make it writable:
<code>m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
</code>

