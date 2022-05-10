import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I expect the <code>m[:]</code> to return <code>b''</code>, but instead it throws a <code>ValueError</code> exception.
Is there a way to make this work as expected?
I need to do this because my code uses <code>mmap</code> a lot, and I want to close it only when the file is not needed anymore. I don't want to close it and re-open it again later.


A:

You can do it with a different approach.
Here is my test code:
<code>import mmap
import os
import time

with open('test', 'wb') as f:
    f.write(bytes(10))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[:])
    f.truncate()
    a = m[:]
    m.resize(0)
    m.close()
</code>
Output:
<code>b'\x00\
