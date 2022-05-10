import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I would expect that the mmap object would be updated to reflect the new file size.
Is there a way to make this work?


A:

The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>The size argument specifies the initial size of the mapped region. If
  size is larger than the file, the file is extended with null bytes.</p>
</blockquote>
So, if you want to truncate the file, you need to specify a size argument to <code>mmap.mmap</code> that is less than the current size of the file.

