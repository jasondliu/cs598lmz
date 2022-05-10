import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code fails with:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
This is because the <code>mmap</code> object is not updated when the file is truncated.
Is there a way to update the <code>mmap</code> object? Or is there a way to create a <code>mmap</code> object with a file that is truncated to zero length?
I am using Python 3.7.3 on Linux.


A:

The <code>mmap</code> object has a <code>resize</code> method.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a
