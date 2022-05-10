import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
</code>
But I get this error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m[0] = b'\x00'
TypeError: 'mmap.mmap' object does not support item assignment
</code>
I'm using Python 3.5.2 on Windows 10.


A:

You need to specify the length of the memory map.
<code>m = mmap.mmap(f.fileno(), 1)
</code>

