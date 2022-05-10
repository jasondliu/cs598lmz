import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: memory mapped size must be positive
</code>
I understand that this is because the file is truncated, but I don't understand why the mmap object is not updated.
Is there a way to update the mmap object?


A:

<code>mmap</code> is not a wrapper around the file, it's a wrapper around the memory mapping of the file.
When you truncate the file, the memory mapping is still there and still has the same size.
You can use <code>mmap.resize()</code> to resize the mapping.

