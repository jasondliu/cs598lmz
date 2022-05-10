import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m[:] = b"a"
</code>
Throws:
<code>Traceback (most recent call last):
  File "test.py", line 13, in &lt;module&gt;
    a = m[:]
ValueError: cannot read memory at 0x7f2247e8f844
</code>

