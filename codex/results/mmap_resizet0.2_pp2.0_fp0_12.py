import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file has been truncated, but I don't understand why the mmap object doesn't get updated.
I'm using Python 3.6.1 on Windows 10.


A:

The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>If <em>length</em> is larger than the current size of the file, the file is extended to contain <em>length</em> bytes. If <em>length</em> is 0, the maximum length of the map is the current size of the file, except that if the file is empty Windows raises an exception (you cannot create an empty mapping on Windows).</p>
</blockquote>
So, the file is extended to contain 1 byte, and the <code>mmap</code> object is created with a length of 1. 
