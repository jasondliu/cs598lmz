import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = bytes(1)
</code>
I get back:
<code>  File "/usr/lib/python3.7/mmap.py", line 238, in __setitem__
    self._write_func(s, offset)
TypeError: 'bytes' does not support the buffer interface
</code>
And when I try:
<code>&gt;&gt;&gt; import mmap
&gt;&gt;&gt; with open('test', 'r+b') as f:
...  m = mmap.mmap(f.fileno(), 0)
...  m[0:1] = bytes(1)
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 2, in &lt;module&gt;
  File "/usr/lib/python3.7/mmap.py", line 238, in __setitem__
    self._write_func(s, offset)
TypeError: 'bytes' does not support the buffer interface
</code>
I get a similar error.
I was looking
