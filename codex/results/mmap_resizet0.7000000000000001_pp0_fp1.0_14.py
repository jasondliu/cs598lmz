import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
Output:
<code>b'\x00'
</code>
So truncating the file does not remove the zeros from the mmap. 
I'm using Python 3.6.7 on Windows 10.


A:

I have no idea why the <code>truncate</code> call is not working, but I don't think the fix is to close the file and reopen it. That would be inefficient, and I think it's not valid on Windows (in the Python implementation).
I think the best approach is to just <code>m.resize</code> the <code>mmap</code> object, using the same technique as in your first question:
<code>#!/usr/bin/env python3

import mmap
import os

os.system('dd if=/dev/urandom of=test bs=1024 count=1024')

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(0)
    print(m[:])

