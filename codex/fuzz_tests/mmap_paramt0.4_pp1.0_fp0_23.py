import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x02'
</code>
I expect to see a file with a single byte of value <code>2</code>, but instead I see a file with a single byte of value <code>1</code>.
I'm using Python 3.5.1 on OS X 10.11.6.


A:

The problem is that the <code>mmap</code> object is not being flushed.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x02'
    m.flush()
</code>

