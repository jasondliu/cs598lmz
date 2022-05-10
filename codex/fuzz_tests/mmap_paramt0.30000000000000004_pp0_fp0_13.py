import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.close()
</code>
This code works fine, but if I change <code>m[0] = b'\x00'</code> to <code>m[0] = b'\x01'</code>, I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    m[0] = b'\x01'
ValueError: byte must be in range(0, 256)
</code>
Why is this? I am using Python 3.6.

