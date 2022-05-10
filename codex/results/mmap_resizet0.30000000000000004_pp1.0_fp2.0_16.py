import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code crashes on the last line with:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I would expect that the mmap object is updated when the file is truncated.
Is there a way to make this work?
(I am using Python 3.6.5 on Windows 10)


A:

This is a bug in Python 3.6.5. It is fixed in Python 3.6.6.

