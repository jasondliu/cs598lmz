import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Traceback:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
How can I truncate the file, while keeping the mmap object?


A:

You can't.
The <code>mmap</code> object is a view onto the file, and you can't change the size of the file without invalidating the <code>mmap</code> object.
If you want to truncate the file, you need to close the <code>mmap</code> object first.

