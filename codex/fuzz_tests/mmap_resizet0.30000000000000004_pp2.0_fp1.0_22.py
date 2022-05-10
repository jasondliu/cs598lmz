import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I have two questions:

Why does <code>mmap</code> raise an exception?
How can I get the contents of the file without raising an exception?



A:

The problem is that the mmap object is not aware of the truncation.  It's still trying to access the file at the original size.
You can fix this by closing the mmap object and reopening it.  This will cause it to be aware of the new file size.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.close()
    m = mmap.mmap(f.fileno(),
