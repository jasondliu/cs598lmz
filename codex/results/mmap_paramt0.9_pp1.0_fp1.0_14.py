import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])

    m[0] = 0
</code>
A couple of things I've managed to figure out:

This works as long as you don't do <code>flush()</code> on the stream.
The change is NOT persisted to disk which is what I really want to happen.

How could I update the file to the desired value?
Edit:
I've tried it this way:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = 0

    m.flush()
</code>
and the file is not updated.


A:

This might be a bit misplaced but I managed to get it working with a <code>deque</code> and <code>mmap</code>. Sample code below:
<code>import mmap

f = open('test', 'wb')
f.write
