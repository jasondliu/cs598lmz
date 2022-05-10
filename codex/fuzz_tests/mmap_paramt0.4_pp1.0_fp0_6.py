import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m[0] = bytes(2)
TypeError: 'bytes' object does not support item assignment
</code>
I'm using Python 3.7.3.


A:

In Python 3, <code>bytes</code> is immutable. You cannot assign to individual bytes of a <code>bytes</code> object.
Use <code>bytearray</code> instead:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytearray(2)
</code>

