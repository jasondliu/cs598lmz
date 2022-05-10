import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This code will raise an exception:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I know that I can use <code>mmap.resize</code> to resize the mmap object, but I want to know why the mmap object is not updated when the file is truncated.


A:

The <code>mmap</code> object is not updated because it is not supposed to be updated.
The <code>mmap</code> object is a view of the file. It is not the file. It is not a copy of the file. It is a view of the file.
When you truncate the file, you are changing the file. You are not changing the <code>mmap</code> object.
The <code>mmap</code> object is a view of the file. It is not the file. It is not a copy of the file. It is a view of the file
