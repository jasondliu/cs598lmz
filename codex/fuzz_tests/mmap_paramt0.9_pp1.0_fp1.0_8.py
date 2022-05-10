import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print m.read(1)
    m.write(b'1')
    m.seek(0)
    print m.read(1)
    m.close()
</code>
rerun: '1'
    b'1'
I suppose I could read the file and then write it back if this is the case, but it would just be cleaner like this.


A:

Here is an official document showing that it is not supported.
A workaround of keeping a tracked buffer in memory is proposed in a comment.

