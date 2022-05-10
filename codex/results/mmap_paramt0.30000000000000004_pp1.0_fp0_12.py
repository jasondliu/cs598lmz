import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.close()
</code>
I get the error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m[0] = b'\x00'
TypeError: 'mmap.mmap' object does not support item assignment
</code>
I'm using Python 3.6.1.


A:

You need to use <code>mmap.ACCESS_WRITE</code> when opening the file.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = b'\x00'
    m.close()
</code>

