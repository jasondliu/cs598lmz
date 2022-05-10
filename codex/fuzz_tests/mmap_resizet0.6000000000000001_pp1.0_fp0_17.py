import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Result:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>


A:

<code>mmap.mmap</code> can't handle the file being truncated, nor can it handle the file being extended.
<code>mmap.mmap</code> is not a replacement for <code>open</code>; it is a replacement for <code>os.open</code>.

1. From the docs:
<blockquote>
<p>If length is larger than the current size of the file, the file is extended with null bytes. This behavior is not portable.</p>
</blockquote>
2. From the docs:
<blockquote>
<p>If length is less than the current size of the file, the file is truncated.</p>
</blockquote>
3. From the source:
<code>if (off &gt;= pylong_from_file_size_t
