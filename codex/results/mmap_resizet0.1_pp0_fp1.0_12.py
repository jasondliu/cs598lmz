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
ValueError: mmap offset is greater than file size
</code>
I would expect the <code>mmap</code> to be updated when the file is truncated. Is there a way to do this?


A:

The <code>mmap</code> object is not updated when the file is truncated.
The <code>mmap</code> object is a view of the file at the time it was created.
If you want to update the <code>mmap</code> object, you need to create a new one.

