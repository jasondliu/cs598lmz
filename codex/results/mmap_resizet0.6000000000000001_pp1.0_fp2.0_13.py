import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The above code produces the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
What should I do to read the file's content?


A:

If you truncate a file, you invalidate all mappings.
From the documentation of <code>mmap.mmap.resize()</code>:
<blockquote>
<p>Note that resizing a file on some systems may invalidate existing mappings in the region that was modified. If you need to use mappings after resizing a file, it may be necessary to create a new mapping, or use mmap.mmap.move() to move the mapping to a new location.</p>
</blockquote>

