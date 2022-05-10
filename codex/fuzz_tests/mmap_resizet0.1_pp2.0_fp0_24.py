import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code works fine on Linux, but on Windows it raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I've tried to use <code>m.resize(0)</code> instead of <code>f.truncate()</code>, but it doesn't help.
Is there a way to truncate a file on Windows without closing the mmap?


A:

The problem is that the <code>mmap</code> object is still referring to the old file size.  You can fix this by calling <code>m.resize(0)</code> after <code>f.truncate()</code>.

