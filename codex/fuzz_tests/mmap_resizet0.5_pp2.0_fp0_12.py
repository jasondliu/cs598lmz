import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This gives:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
However, if I do:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    f.truncate()
</code>
It works fine.
My question is, why does the first example give an error? Is it undefined behavior to mmap a file, truncate it and then read from the mmap?
I'm using Python 2.7.6 on Ubuntu 14.04.


A:

I think this is because you're trying to access the mmap after you've truncated the file.  It's not clear to me from the docs whether this is allowed or not.

