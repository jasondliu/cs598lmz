import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
</code>
This raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m[0] = bytes(2)
TypeError: 'str' does not support the buffer interface
</code>
What am I doing wrong?


A:

You can't assign to a slice of a <code>mmap</code> object. Use <code>write</code> instead:
<code>m.write(bytes(2))
</code>

