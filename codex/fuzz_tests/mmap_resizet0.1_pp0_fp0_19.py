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
I understand that the file size is 0, but I don't understand why the mmap offset is greater than the file size.
I'm using Python 3.6.5 on Windows 10.


A:

The problem is that you are using <code>mmap.mmap</code> with a length of 0.
<code>mmap.mmap</code> takes a length argument, which is the length of the memory map. If you pass 0, it will map the entire file.
If you pass a length of 0, and then truncate the file, the memory map will be invalidated.
If you pass a length of 1, then the memory map will be valid after truncating the file.

