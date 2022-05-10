import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This code throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
But if I comment out the line <code>f.truncate()</code> or the line <code>a = m[:]</code> the code works fine.
I know that the mmap object is invalidated after the file is truncated, but I don't understand why the code throws an exception when I try to read from the mmap object, but not when I truncate the file.
I'm using Python 3.6.3 on Windows 10.


A:

The problem is that the <code>mmap</code> object is still referencing the original file size, even though the file has been truncated.
When you try to read from the <code>mmap</code> object, it tries to read the original size of the file, which is now invalid.
When you truncate the file, the <code
