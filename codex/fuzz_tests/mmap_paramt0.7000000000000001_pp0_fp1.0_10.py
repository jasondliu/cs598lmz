import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write(bytes(255))
</code>
but this gives error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m.write(bytes(255))
ValueError: write() argument must be a bytes-like object
</code>
If I use <code>bytes(255)</code> to initialize the file, the error disappears.
What wrong with my code?

