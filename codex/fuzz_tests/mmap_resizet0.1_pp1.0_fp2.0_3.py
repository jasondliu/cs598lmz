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
I understand that the file size is 0, but I don't understand why the offset is greater than the file size.
I'm using Python 3.6.4 on Windows 10.


A:

The problem is that you are using <code>mmap.mmap(f.fileno(), 0)</code>. The second argument is the size of the mapping. If you pass <code>0</code>, the size of the mapping is the size of the file.
So, when you truncate the file, the size of the mapping is still the size of the file before truncation.
You can use <code>mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)</code> to get a mapping that is always the size of the file.

