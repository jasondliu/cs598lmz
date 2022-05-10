import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
gives
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: memory mapping closed or invalid
</code>
Why is the <code>mmap</code> object invalidated when the file is truncated?
I am using Python 3.6.1 on Ubuntu 16.04.


A:

The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>If <em>length</em> is larger than the current size of the file, the file is extended to contain <em>length</em> bytes. If <em>length</em> is 0, the maximum length of the map is the current size of the file, except that if the file is empty Windows raises an exception (you cannot create an empty mapping on Windows).</p>
</blockquote>
So when you truncate the file, the mapping is no longer valid.

