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
ValueError: mmap length is zero
</code>
I understand that the mmap object is not aware of the truncation, but I would expect it to be able to read the data that was there before the truncation.
Is there a way to do this?


A:

The <code>mmap</code> object is not aware of the truncation because it is not aware of the file at all. It is a view of the memory mapped to the file, and the memory is not aware of the file either.
If you want to read the data that was there before the truncation, you have to read it before the truncation.

