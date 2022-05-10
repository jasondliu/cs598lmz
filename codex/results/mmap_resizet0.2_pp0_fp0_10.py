import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I would expect it to return an empty string.
Is this a bug or am I doing something wrong?


A:

The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>The file’s size cannot be changed while mmap() is in use.</p>
</blockquote>
You are using <code>mmap</code> in the <code>with</code> block, so it is in use.

