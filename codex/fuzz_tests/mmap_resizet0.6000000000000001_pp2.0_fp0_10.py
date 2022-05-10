import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code works as expected in python 3.6.2, but in python 2.7.12 (both on Ubuntu 16.04) I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 12, in &lt;module&gt;
    a = m[:]
TypeError: slice indices must be integers or None or have an __index__ method
</code>
So I'm assuming this is a bug in python 2.7.12. Is it and is there a workaround?

