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
  File "test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
I'm using Python 3.6.5 on Windows 10.
I can't find any documentation on this. Is this a bug or is there a way to get the data from the mmap object?


A:

This is a bug in Python 3.6.5. It is fixed in Python 3.7.

