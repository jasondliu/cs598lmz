import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.close()
</code>
However, this yields an error:
<code>Traceback (most recent call last):
  File "a.py", line 9, in &lt;module&gt;
    m[0] = b'\x00'
TypeError: 'mmap.mmap' does not support the buffer interface
</code>
What am I doing wrong?

