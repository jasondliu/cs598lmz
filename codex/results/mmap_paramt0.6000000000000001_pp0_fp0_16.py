import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(2)
</code>
I get the error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m.resize(2)
OSError: [Errno 22] Invalid argument
</code>
I am using Python 3.4.1


A:

You cannot resize the file using <code>mmap</code> on Windows. The <code>mmap</code> module on Windows does not support the <code>resize()</code> method.
According to the Python documentation:
<blockquote>
<p>The <code>&lt;code&gt;resize()&lt;/code&gt;</code> method is currently only implemented on Unix, and only for anonymous maps created with <code>&lt;code&gt;mmap.MAP_ANONYMOUS&lt;/code&gt;</code>.</p>
</blockquote>

