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
I understand that the file size is 0, but I don't understand why the mmap offset is greater than the file size.
I'm using Python 3.6.1 on Windows 10.


A:

The problem is that the <code>mmap</code> object is not updated when you truncate the file.
You can see this by printing the <code>mmap</code> object:
<code>&gt;&gt;&gt; m
&lt;mmap.mmap object at 0x7f7e9f8c5a00&gt;
</code>
You can see that the <code>mmap</code> object is still pointing to the old file size.
You can fix this by calling <code>m.resize()</code> after truncating the file:
<code>with open('test
