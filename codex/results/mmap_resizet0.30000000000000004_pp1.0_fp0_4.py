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
I understand that the mmap object is not aware that the file was truncated.
Is there a way to update the mmap object to reflect the new file size?
I'm using Python 3.6.


A:

<code>mmap.mmap</code> has no method to update the file size.
You can use <code>mmap.resize</code> to resize the mmap object and you can use <code>mmap.resize</code> to resize the underlying file.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    mmap.resize
