import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
</code>
This is the error I get:
<code>Traceback (most recent call last):
  File "test.py", line 7, in &lt;module&gt;
    m[0] = bytes(2)
TypeError: must be read-write buffer, not bytes
</code>
I'm running Python 3.6.1 on Windows 10.

