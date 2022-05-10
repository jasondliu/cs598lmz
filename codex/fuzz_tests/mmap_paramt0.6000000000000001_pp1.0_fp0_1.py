import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0]
</code>
It is returning <code>mmap.error: [Errno 9] Bad file descriptor</code>
Can someone explain me why?


A:

You are getting an error because you are trying to access the mapping before calling <code>mmap.mmap</code>. The file descriptor is closed when the file object is destroyed.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0]
</code>
The above code is equivalent to:
<code>f = open('test', 'r+b')
m = mmap.mmap(f.fileno(), 0)
f.close()
m[0]
</code>
<code>f.close()</code> closes the file descriptor and <code>m[0]</code> fails because the underlying file descriptor is closed.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)

m
