import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
</code>
I get the following error:
<code>TypeError: an integer is required
</code>
I'm using Python 3.3.2 on Ubuntu 13.04.


A:

The problem is that you're using <code>bytes</code> instead of <code>bytearray</code>.
<code>bytes</code> is immutable, so you can't assign to <code>m[0]</code>.
<code>&gt;&gt;&gt; m = mmap.mmap(-1, 1)
&gt;&gt;&gt; m[0] = b'\x01'
&gt;&gt;&gt; m[0]
1
&gt;&gt;&gt; m = mmap.mmap(-1, 1)
&gt;&gt;&gt; m[0] = bytes([1])
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: an
