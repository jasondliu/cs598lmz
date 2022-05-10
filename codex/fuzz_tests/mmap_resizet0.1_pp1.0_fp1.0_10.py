import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I would expect the <code>mmap</code> to be updated when the file is truncated.
Is there a way to make this work?


A:

You can't use <code>mmap</code> to map a file that is smaller than the <code>mmap</code> object.
<code>mmap</code> is a memory-mapped file, and it is a view of the file.  If the file is smaller than the <code>mmap</code> object, then the <code>mmap</code> object is trying to map memory that doesn't exist.
If you want to truncate the file, you need to unmap the <code>mmap</code> object first.

