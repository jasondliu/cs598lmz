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
I understand that the file size is 0, but I thought that the mmap would be updated to reflect the new file size.
Is there a way to get the mmap to reflect the new file size?


A:

The <code>mmap</code> object is not updated when the file is truncated.  You need to create a new <code>mmap</code> object.

