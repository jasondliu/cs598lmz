import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 65
    m.close()
</code>
Output:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    m[0] = 65
TypeError: 'mmap.mmap' does not support the buffer interface
</code>


A:

You need to open the file with the write flag.
<code>m = mmap.mmap(f.fileno(), 0, access = mmap.ACCESS_WRITE)
</code>

