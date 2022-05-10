import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
It is not that easy to understand why <code>m[:]</code> works but not <code>m[0]</code>. I guess it is because Python is interpreting <code>m[0]</code> as a getter. My expectation is that the first <code>0</code> should be interpreted as the file descriptor 0. Is there some way to fix this? Can it be seen as a bug? I know this is not a common use case, but maybe someone knows a fix.


A:

Here is how to do this
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
But it is longer. My expectation is that truncating a file will reduce the number of bytes the mmap object is able to access.

