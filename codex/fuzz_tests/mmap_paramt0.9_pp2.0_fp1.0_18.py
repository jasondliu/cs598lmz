import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write_byte(bytes(1))
</code>
I get an error:
<code>Traceback (most recent call last):
  File "C:/Downloads/untitled/test.py", line 9, in &lt;module&gt;
    m.write_byte(bytes(1))
TypeError: Expected a byte value
</code>
What is wrong here?


A:

In Python 3, <code>bytes</code> is a class which is immutable, so <code>bytes(1)</code> is equivalent to <code>bytes(b'\x00'</code>), which means that <code>bytes(1)</code> will be a single zero byte.  <code>m.write_byte()</code> expects to be given a byte-sized value, so you want <code>m.write_byte(b'\x01'</code>).  Note that <code>bytes(1)</code> actually uses two characters in the code, not one, because the <code>\x</code> escapes count.  Alternatively, if you just wanted to write
