import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write_byte(bytes(3))
</code>
I get the following exception:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    m.write_byte(bytes(3))
TypeError: must be convertible to a buffer, not bytes
</code>
How can I write to a mmap object with one byte?


A:

Your <code>bytes</code> is actually a <code>str</code> in Python 3 and it needs to be a <code>bytes</code> (or <code>bytearray</code>).
Try:
<code>m.write_byte(b'3')
</code>

