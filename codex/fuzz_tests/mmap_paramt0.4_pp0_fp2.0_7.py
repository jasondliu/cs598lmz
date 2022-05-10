import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
</code>
But, this is not working.
<code>Traceback (most recent call last):
  File "test.py", line 7, in &lt;module&gt;
    m[0] = b'\x00'
TypeError: write() argument must be str, not bytes
</code>
Is there a way to write bytes to a mmap object?


A:

<code>mmap</code> objects are read-only by default. You need to pass <code>access=mmap.ACCESS_WRITE</code> to the <code>mmap</code> constructor.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = b'\x00'
</code>

