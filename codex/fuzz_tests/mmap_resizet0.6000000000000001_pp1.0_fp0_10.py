import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises the exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
If you instead use the <code>mmap.MAP_NORESERVE</code> flag to create the <code>mmap</code> object, then you can shrink the file to zero bytes, but then the <code>mmap</code> access raises <code>IndexError: memory index out of range</code>.
Note that this is not a problem if you're using <code>mmap</code> to grow the file (as is the common case when you're using it to create a memory-mapped database).

