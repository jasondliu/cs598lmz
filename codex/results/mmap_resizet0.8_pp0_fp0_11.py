import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises an exception:
<code>Traceback (most recent call last):
  File "mmap.py", line 10, in &lt;module&gt;
    a = m[:]
IndexError: index out of range
</code>
What is the best way to do this?


A:

You can't do it. The <code>mmap</code> is tied to the file, and it cannot be extended since you truncated it.
If you instead extend it, then you can close the <code>mmap</code> and then create a new one.

