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
ValueError: mmap offset is greater than file size
</code>
I understand that the file is truncated and the mmap is invalidated. But I don't understand why I can't read from it.
I would expect that the mmap is still valid, but the file is truncated and the mmap is just a view of the truncated file.
Is there a way to make it work?


A:

The mmap is invalidated because the file size is now 0. The mmap is a view of the file, and the view is no longer valid.
You can't read from it because the mmap is invalid.

