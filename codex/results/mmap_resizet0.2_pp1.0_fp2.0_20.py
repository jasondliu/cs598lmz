import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This code raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I understand that the file is truncated, but I don't understand why the mmap object is not updated.
I'm using Python 3.6.3 on Windows 10.


A:

The <code>mmap</code> object is not updated because it is not supposed to be updated.
The <code>mmap</code> object is a view of the file at the time it was created.
If you want to update the <code>mmap</code> object, you need to create a new one.

