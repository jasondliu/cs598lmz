import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>

I am aware of the following questions:

ValueError: invalid length for mmap: 0
Truncate file while mmap'ed

When the file is open for read, the result is:
<code>Environment: CPython 3.4.3, Darwin 14.1.0, 64bit

Traceback (most recent call last):
  File "./test.py", line 10, in &lt;module&gt;
    m = mmap.mmap(f.fileno(), 0)
ValueError: invalid length for mmap: 0
</code>
When the file is open for read and write, the result is:
<code>Environment: CPython 3.4.3, Darwin 14.1.0, 64bit

Traceback (most recent call last):
  File "./test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: mmap closed or invalid
</code>

How do I truncate a file while an mmap is held?


A:

You need to use the <code>res
