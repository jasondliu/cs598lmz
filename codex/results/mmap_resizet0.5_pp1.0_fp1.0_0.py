import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This fails with the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
The problem is that the file has been truncated to 0 bytes, but the mmap object still thinks it's 1 byte long.
Is there a way to make the mmap object aware of the new file size?


A:

The answer is in the documentation:
<blockquote>
<p>The file must be opened in read/write (r+), read-only (r), or write-only (w+ or w) mode.</p>
</blockquote>
You should open the file in <code>w+</code> mode.
<code>with open('test', 'w+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>

