import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Output:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file pointer is moved to the end of the file, but I thought that the mmap would be unaffected by this. 
I am using Python 3.6.1 on Windows 10.


A:

You need to use <code>mmap.resize</code> to change the size of the memory map.

