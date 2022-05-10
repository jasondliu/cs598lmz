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
I'm using Python 3.4.3 on Windows 7.
I'm trying to understand why this is happening. I'm guessing that the <code>mmap</code> object is still using the old file size, but I'm not sure.
I'm also wondering if there is a way to get around this. I'm trying to use <code>mmap</code> to read a file that is being written to by another process. I want to be able to read the file as it is being written to. I'm not sure if this is possible.


A:

The <code>mmap</code> object is still using the old file size.
The <code>mmap</code> object is not aware of the file size change.
You can use <code>m.resize(new_size)</code> to resize the <code>mmap</
