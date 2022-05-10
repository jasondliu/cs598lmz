import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] #should not be b''
</code>
Opening the file using <code>mmap</code> does not change the behaviour. So I am wondering if there is a way to achieve what I want.


A:

The docs for <code>mmap</code> say
<blockquote>
<p>The data attribute is a byte string that can be used to read or modify the mapped region</p>
</blockquote>
and you appear to be doing the latter, which isn't allowed:
<code>&gt;&gt;&gt; m = mmap.mmap(f.fileno(), 0)
&gt;&gt;&gt; m[:] = b''
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: must be read-only buffer, not memoryview
</code>
There is no easy way to truncate a file in general, as it involves moving the beginning of every block of data in the file (by zero or more bytes), which could be a lot of work.
You could work around
