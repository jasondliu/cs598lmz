import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.close()
</code>
I get the error
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m[0] = b'\x00'
ValueError: byte must be in range(0, 256)
</code>
I am not sure what I am doing wrong.


A:

You are trying to assign a byte to a byte - so you need to assign an integer.
<code>m[0] = 0
</code>

