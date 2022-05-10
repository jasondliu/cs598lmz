import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0
</code>
Gives:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m[0] = 0
ValueError: must be a bytes-like object, not 'int'
</code>
I have read a few other questions related to this error but can't figure out how to write to the memory mapped file.

