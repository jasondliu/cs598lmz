import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0
</code>
<code>Traceback (most recent call last):
  File "test.py", line 6, in &lt;module&gt;
    m[0] = 0
ValueError: memory mapping assignment must be the same size as memory mapping slice
</code>

