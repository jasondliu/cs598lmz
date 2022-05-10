import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
</code>
If you run python3 right after python2 with this code the second run fails with the error
<code>Traceback (most recent call last):
  File "./pymmap.py", line 8, in &lt;module&gt;
    m = mmap.mmap(f.fileno(), 0)
ValueError: cannot mmap an empty file
</code>
Conversely, if you run python2 right after python3 again it fails with the same error.
Any insight would be appreciated.

