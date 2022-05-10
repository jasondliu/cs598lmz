import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The last line throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: mmap closed or invalid
</code>
I don't understand why. The documentation says that the mmap object is still valid after a truncate.


A:

The documentation says:
<blockquote>
<p>If the file is resized by another process, the mmap object can be resized as follows (assuming that fd is the original file descriptor):</p>
<pre><code>&lt;code&gt;m.close()
m = mmap.mmap(fd, 0)
&lt;/code&gt;</code></pre>
</blockquote>
So you should close the mmap object and reopen it.

