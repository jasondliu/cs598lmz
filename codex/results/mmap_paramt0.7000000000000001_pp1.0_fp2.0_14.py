import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0x01
    m.close()
</code>
The output is:
<code>Traceback (most recent call last):
  File "mmap_test.py", line 9, in &lt;module&gt;
    m[0] = 0x01
TypeError: 'mmap.mmap' does not support the buffer interface
</code>
Why does this happen?


A:

<code>bytes</code> is a type in Python 3.x, not a function. 
<code>bytes([1]) # Python 2.x
b'\x01'

bytes([1]) # Python 3.x
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: 'bytes' object is not callable
</code>
You can use <code>bytearray</code> to create a sequence of bytes in Python 3.x.
<code>bytearray([1])
bytearray(b'\x01')
