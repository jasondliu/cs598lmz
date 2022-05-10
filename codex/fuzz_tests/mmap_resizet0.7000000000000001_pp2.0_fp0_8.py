import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Here is the traceback:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 4, in &lt;module&gt;
ValueError: Cannot use mmap on files with zero size.
</code>


A:

See my comments on the question.
<code>#!/usr/bin/env python3
import mmap

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>

