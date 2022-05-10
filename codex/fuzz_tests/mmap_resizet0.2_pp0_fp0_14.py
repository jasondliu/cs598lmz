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
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I would like to know if there is a way to get the data from the mmap object after truncating the file.


A:

The <code>mmap</code> object is a view of the file.  When you truncate the file, the view is no longer valid.
You can use <code>mmap.resize</code> to resize the view, but it will be empty.

