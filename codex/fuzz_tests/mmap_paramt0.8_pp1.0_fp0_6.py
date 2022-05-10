import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[1] = b'\x00'
    m.resize(3)
    m[2] = b'\x00'
    m.close()
</code>
which gives the bytes '\x01\x00\x00'.
If you try to resize to 1 byte in the example above, you get
<code>&gt;&gt;&gt; with open('test', 'r+b') as f:
...     m = mmap.mmap(f.fileno(), 0)
...     m.resize(1)
...     m.close()
... 
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 3, in &lt;module&gt;
OSError: [Errno 22] Invalid argument
</code>
The <code>mmap.mmap</code> documentation says
<blockquote>
<p>A <code>&lt;code&gt;mmap&lt;/code&gt;</code> object is a window into a file.</p>
</blockquote>
