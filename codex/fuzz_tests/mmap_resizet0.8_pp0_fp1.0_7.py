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
Or in Python 2, this works:
<code>from __future__ import print_function

import mmap

with open('test', 'wb') as f:
    f.write(chr(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
Output:
<code>'\x01'
</code>

