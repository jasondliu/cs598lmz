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
I understand that the file size is 0, but I don't understand why the mmap offset is greater than the file size.
I'm using Python 3.5.2 on Windows 10.


A:

The problem is that you're using <code>mmap.mmap</code> with a length of 0.
<code>m = mmap.mmap(f.fileno(), 0)
</code>
This means that the mmap object is created with a length of 0 bytes.  This is why you get the error when you try to access the mmap object.
If you want to create a mmap object that is the same size as the file, you can use the <code>mmap.ALLOCATIONGRANULARITY</code> constant.  This constant is the size of the smallest unit of memory that can be allocated.  You can
