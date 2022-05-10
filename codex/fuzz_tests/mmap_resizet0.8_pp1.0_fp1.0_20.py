import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
and got
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m = mmap.mmap(f.fileno(), 0)
OSError: [Errno 22] Invalid argument
</code>
Why?


A:

Try this:
<code>#!/usr/bin/env python

import mmap
import os

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), os.fstat(f.fileno()).st_size)
    f.truncate()
    a = m[:]
</code>
The problem here is that you are asking mmap to create a mapping of size 0, which is not valid. The solution is to use the actual file size.
Note that the resulting mapping (which is empty) will be mapped to the current end-of-file position. This means that any growth in the
