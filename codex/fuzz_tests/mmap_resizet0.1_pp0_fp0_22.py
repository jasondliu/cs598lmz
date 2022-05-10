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
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file size is 0, but I don't understand why the mmap offset is greater than the file size.
I'm using Python 3.6.5 on Windows 10.


A:

The problem is that you're using <code>mmap.mmap</code> with a length of 0. This means that the mmap object is empty, and so the offset is greater than the file size.
You can fix this by using <code>mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)</code> instead. This will create a mmap object that is the same size as the file.

