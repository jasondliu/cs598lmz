import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(0)
</code>
But this doesn't work:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    m[0] = bytes(0)
TypeError: must be read-write buffer, not mmap
</code>
How should I do this?


A:

You need to set the access mode to read-write:
<code>m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
</code>

