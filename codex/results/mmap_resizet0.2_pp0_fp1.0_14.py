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
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file size is 0, but I don't understand why the mmap offset is greater than the file size.
I am using Python 3.6.1 on Windows 10.


A:

The problem is that you're using <code>mmap.mmap</code> to create a memory-mapped object that is the same size as the file.  When you truncate the file, the memory-mapped object is still the same size, and the offset is still the same.  But the file is now smaller, so the offset is now greater than the file size.
If you want to create a memory-mapped object that is the same size as the file, you need to use <code>mmap.mmap</code> with the <code>length</code> argument set to 0.  Then the memory-
