import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Throws
<code>Traceback (most recent call last):
  File "/usr/bin/python3", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero, cannot slice
</code>

