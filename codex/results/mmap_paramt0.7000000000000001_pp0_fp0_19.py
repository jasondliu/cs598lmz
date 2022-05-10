import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0
</code>
The error being:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    m[0] = 0
TypeError: 'mmap.mmap' does not support the buffer interface
</code>
I can't find anything in the docs about this. Is it something I am doing wrong, or is it just not possible?


A:

This is not supported.
The docs of <code>mmap.mmap</code> say:
<blockquote>
<p>Provide an array-like view of a file or other object. The memory
  mapping is created using the <code>&lt;code&gt;mmap()&lt;/code&gt;</code> function in the <code>&lt;code&gt;mmap&lt;/code&gt;</code> module.</p>
</blockquote>
You can use <code>mmap.mmap</code> to expose a file-like interface and use that as a buffer. 
