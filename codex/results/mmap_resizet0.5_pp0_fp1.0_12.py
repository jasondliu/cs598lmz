import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
It seems like mmap should be able to handle this case. Is this a bug or is there something I'm doing wrong?


A:

This is a bug in Python. The problem is that the offset is not updated when the file is truncated.
<code>In [1]: import mmap

In [2]: with open('test', 'wb') as f:
   ...:     f.write(bytes(1))
   ...:

In [3]: with open('test', 'r+b') as f:
   ...:     m = mmap.mmap(f.fileno(), 0)
   ...:     print(m.offset)
   ...:     f.truncate()
   ...:     print(m.offset)
   ...:     a = m[:]
   ...:
0

