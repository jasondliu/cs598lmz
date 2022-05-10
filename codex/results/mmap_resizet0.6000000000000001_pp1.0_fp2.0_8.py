import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code worked fine on Python 3.4 and 3.5, but fails on 3.6:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap slice assignment is larger than memory
</code>
I'm using Python 3.6.3 on Ubuntu 16.04.1.


A:

I got the same error using python 3.6.2 on Ubuntu.
I was able to fix it by adding <code>m.resize(0)</code> before <code>f.truncate()</code>

