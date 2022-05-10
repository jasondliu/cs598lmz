import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'2'
    m.close()
</code>
But, when I try to run it, it raises the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.4/mmap.py", line 287, in __setitem__
    self.write(item)
TypeError: memoryview: a bytes-like object is required, not 'str'
</code>
According to documentation, it should work. What am I doing wrong?


A:

<code>m[0] = b'2'
</code>
<code>b'2'</code> is a bytes literal which becomes a <code>bytes</code> object. This is not what <code>mmap</code> wants, it wants a <code>bytearray</code>.
<code>m[0] = bytearray(b'2')
</code>
is what you want.

