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
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
I understand that the error is caused by the fact that the file is empty, but I don't understand why this happens.
I thought that the <code>mmap</code> object is just a view of the file, so it should not be affected by the truncation.
Is there a way to avoid this error?


A:

I think the problem is that the <code>mmap</code> object is not a view of the file, but a view of the file descriptor.
If you use <code>mmap.mmap(0, 0)</code> instead of <code>mmap.mmap(f.fileno(), 0)</code> it works.

