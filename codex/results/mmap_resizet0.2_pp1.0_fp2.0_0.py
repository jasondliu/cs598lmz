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
ValueError: mmap offset is greater than file size
</code>
I would expect that the mmap object would be updated when the file is truncated. Is this a bug or am I doing something wrong?


A:

The <code>mmap</code> object is not updated when the file is truncated.
The documentation for <code>mmap</code> says:
<blockquote>
<p>The file size cannot change while the file is mapped.</p>
</blockquote>

