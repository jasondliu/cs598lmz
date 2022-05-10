import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
The same code works fine on Python 2.7.
Is this a bug in Python 3.6?


A:

This is because the underlying <code>mmap</code> object is closed when you call <code>truncate</code>.
From the documentation:
<blockquote>
<p>If the file is resized, the mmap is resized to the new size as well. If the file is resized to a larger size, the new size is not accessible from the mmap object until the corresponding memory is accessed. If the file is resized to a smaller size, the mmap object is resized to the new size, and the extra memory is discarded. If the file is closed, the mmap object is also closed.</p>
</blockquote>

