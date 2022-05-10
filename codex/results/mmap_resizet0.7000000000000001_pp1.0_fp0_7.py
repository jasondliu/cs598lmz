import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code works in Python 2.7.6, but in Python 3.4.3 throws exception:
<code>ValueError: mmap offset is greater than file size
</code>


A:

One of my tests on Python 3.4.3 is this one:
<code>from mmap import mmap
from tempfile import NamedTemporaryFile

with NamedTemporaryFile() as temp:
    fd = temp.fileno()
    with mmap(fd, 0) as mm:
        temp.truncate(0)
        mm.seek(0)
        print(repr(mm.read(1)))
</code>
The output is: <code>b''</code>
<code>import mmap
import tempfile

with tempfile.NamedTemporaryFile() as temp:
    fd = temp.fileno()
    with mmap.mmap(fd, 0) as mm:
        temp.truncate(0)
        mm.seek(0)
        print(repr(mm.read(1)))
</code>

