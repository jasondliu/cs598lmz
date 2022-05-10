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
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
What is the right way of doing this?


A:

You can't.
The <code>mmap</code> module is a wrapper around the <code>mmap</code> system call, and the <code>mmap</code> system call requires that the file be non-empty.

