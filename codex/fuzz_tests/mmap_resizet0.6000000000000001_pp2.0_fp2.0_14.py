import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I'm getting an error:
<code>Traceback (most recent call last):
  File "mmap.py", line 7, in &lt;module&gt;
    a = m[:]
ValueError: mmap slice assignment is wrong size
</code>
Why is this happening? I'm assuming that the mmap is not yet aware of the truncated file size. Is there a way to make it aware? Why doesn't <code>mmap</code> value update automatically?


A:

The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>If <em>length</em> is omitted, the maximum length possible based on the file’s current size, the <em>access</em> flags and the host system’s page size is used.</p>
</blockquote>
When you truncate the file, the <code>mmap</code> object still has the old length.
<code>m.resize(0)
</code>
will make it aware of the new length.

