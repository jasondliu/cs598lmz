import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
Error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>


A:

This is a limitation of <code>mmap</code>. From documentation:
<blockquote>
<p>When modifying a memory mapped array, changes are limited to the
  range that was initially mapped.</p>
</blockquote>

