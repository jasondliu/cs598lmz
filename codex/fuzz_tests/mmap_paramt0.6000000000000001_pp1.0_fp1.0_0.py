import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = b'1'
    m.close()
</code>
This works, but when I try to do it with a <code>namedtuple</code>, it fails:
<code>from collections import namedtuple
import mmap

Point = namedtuple('Point', 'x y')
with open('test', 'wb') as f:
    f.write(bytes(Point(1, 2)))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = bytes(Point(2, 3))
    m.close()
</code>
I get the error:
<code>TypeError: 'Point' does not support the buffer interface
</code>
What is the reason for this?


A:

You are trying to write a <code>Point</code> to the mmap, not a <code>bytes</code> object.
The <code>bytes
