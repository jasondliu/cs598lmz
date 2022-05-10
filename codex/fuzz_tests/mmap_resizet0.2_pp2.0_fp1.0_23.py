import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I would expect the mmap to be updated to reflect the truncation.
Is this a bug or am I doing something wrong?
I'm using Python 3.6.4 on Windows 10.


A:

This is a known bug in Python 3.6.4, fixed in Python 3.6.5.

