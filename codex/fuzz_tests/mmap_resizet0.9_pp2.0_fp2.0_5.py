import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get <code>ValueError: cannot resize mmap object</code>.
I can't seem to find any docs on manimap() that talk about this, but it does appear to do what I expect:
<code>from mmap import mmap, ACCESS_WRITE
from os import close, unlink 
from tempfile import mkstemp
from uuid import uuid4

filename = mkstemp()[1]
with open(filename, 'w+') as f:
    f.write("testing")
    f.flush()
    mm = mmap(f.fileno(), 1, access=ACCESS_WRITE)
    unlink(filename)
    close(f.fileno())
    f.close()
# without the call to unlink, I get the same error
    mm.resize(42)
    print(mm[5])
</code>
Weirdly, if I don't close one of the file descriptors, I get the same error.  I can't find a reference that says that a file must be closed if using manual entry with <code>mmap
