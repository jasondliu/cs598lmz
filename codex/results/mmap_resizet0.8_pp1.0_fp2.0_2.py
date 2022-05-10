import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line above (<code>a = m[:]</code>) causes the following exception to be raised:
<code>Traceback (most recent call last):
  File "test_blob_bug.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: read only buffer
</code>
From the mmap docs:
<blockquote>
<p>readonly is an optional flag which is False by default. It specifies whether changes to the file’s data should be written through to the original file. If this argument is False, changes to the mmap object are written to an in-memory buffer and flushed to the original file when the mmap is resized or closed. If this argument is True, changes to the mmap object are written directly to the original file.</p>
</blockquote>
I think the documentation is misleading. It seems that the <code>readonly</code> flag applies only to the changes to the mmap'ed data and not to the underlying file. From the docs:
<blockquote>
<p>close()</p>
<p>
