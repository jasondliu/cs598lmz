import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises the exception:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 5, in &lt;module&gt;
ValueError: mmap length is zero
</code>
How to fix this?


A:

You can't.  The mmap object is now invalid.  You have to create a new one.  See the docs.

