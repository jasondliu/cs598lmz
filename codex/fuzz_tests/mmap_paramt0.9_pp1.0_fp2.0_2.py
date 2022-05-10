import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    m[0] = b'Y'
</code>
This code gives me an error: <code>TypeError: must be read-write bytes-like object, not int</code>

<code>&gt;&gt;&gt; m = mmap.mmap(f.fileno(), 1)
&gt;&gt;&gt; m
&lt;mmap.mmap at 0x10c9a2d28&gt;
&gt;&gt;&gt; m[0]
88
&gt;&gt;&gt; m[0] = 88
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: must be read-write bytes-like object, not int
&gt;&gt;&gt; m[0] = b'A'
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: must be read-write bytes-like object
