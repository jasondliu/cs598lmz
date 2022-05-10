import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
And this is the output:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I can't understand why this error is happening. The mmap object should contain the whole file's contents.


A:

From the docs:
<blockquote>
<p>mmap.mmap(fileno, length[, tagname[, access[, offset]]])</p>
</blockquote>
<code>offset</code> is the offset in bytes into the file. By default, it is 0.
<blockquote>
<p>The optional fileno specifies a file descriptor and requires the length argument to be specified.</p>
</blockquote>
So you're asking for a memory-mapped view of the file starting at 1, which is the equivalent of writing <code>m = mmap.mmap(f.fileno(), 1, offset=1)</code>

