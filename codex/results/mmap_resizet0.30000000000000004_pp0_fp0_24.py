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
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I understand that the mmap object is no longer valid after the file is truncated, but I don't understand why I can't access the data before the file is truncated.  I'm using Python 3.4.


A:

<code>mmap</code> is not a file object, it is a memory object.  It is not a copy of the file, it is a view of the file.  When you truncate the file, the memory object is no longer valid.

