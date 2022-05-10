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
I understand that the file size is 0 after truncate, but why is the mmap offset greater than the file size?


A:

The offset is the offset of the mapping in the file.  It's not the offset of the file in the mapping.  The offset is 0 in your case, so the mapping is at the beginning of the file.
The mapping is still valid, but it's empty.  You can't read from it, but you can write to it.

