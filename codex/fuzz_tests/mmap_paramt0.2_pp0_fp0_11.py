import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
</code>
This is the error I get:
<code>Traceback (most recent call last):
  File "mmap_test.py", line 8, in &lt;module&gt;
    m[0] = b'\x00'
TypeError: write() argument must be str, not bytes
</code>
I'm using Python 3.5.2 on Windows 10.


A:

The error message is misleading. The problem is that you are trying to write to a read-only memory map.
<code>mmap.mmap(f.fileno(), 0)</code> creates a read-only memory map. You need to pass <code>mmap.ACCESS_WRITE</code> to the <code>access</code> argument to create a writable memory map.
<code>m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
</code>

