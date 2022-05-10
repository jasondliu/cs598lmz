import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This raises <code>mmap.error: [Errno 6] No such device or address</code>.
Apparently this is an intentional feature of the Python mmap module. See this.
In any case, is there a way to accomplish this by changing the mmap module or doing something before truncation?
Update:
I also tried <code>f.truncate(0)</code> and <code>f.seek(0)</code>, both raise the same <code>mmap.error: [Errno 6] No such device or address</code>.
I am using Python 3.3.2 on Linux (Ubuntu).


A:

I think this is a bug in Python's implementation of <code>mmap.mmap</code>.
Take a look at the following code snippet taken from the official end of file handling documentation on mmaps:
<code>from mmap import mmap, ACCESS_WRITE, SEEK_END
from os import SEEK_SET, remove
from os.path import getsize

with open('new_file', 'w') as f:

