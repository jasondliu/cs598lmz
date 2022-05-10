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
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap slice assignment is wrong size
</code>
I understand that the mmap is not updated when the file is truncated. But I don't understand why I get this error when trying to read from the mmap.
I'm using Python 3.6.5 on Ubuntu 18.04.


A:

The documentation says:
<blockquote>
<p>If the file is resized, the mmap will reflect the new size, even if the file is resized from another process.</p>
</blockquote>
So you can't just truncate the file and expect the mmap to be valid. You have to unmap it first.
<code>m.close()
f.truncate()
</code>

