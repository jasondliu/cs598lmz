import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(1)
</code>
This is the error I am receiving:
<code>Traceback (most recent call last):
  File "/home/user/Desktop/test.py", line 8, in &lt;module&gt;
    m[0] = bytes(1)
TypeError: 'str' does not support the buffer interface
</code>
I have also tried this with <code>bytearray(1)</code> and <code>bytes(1)</code>. What am I doing wrong?


A:

The problem is that the <code>bytes</code> object that you're trying to assign is a single-character string, not a raw byte. To fix the problem, use the <code>chr</code> function to convert a code point to a byte:
<code>m[0] = chr(1)
</code>
Note that in Python 3, <code>chr</code> is deprecated and you should use <code>bytes</code> instead:
<code>m[0] = bytes((1,))
</code>

