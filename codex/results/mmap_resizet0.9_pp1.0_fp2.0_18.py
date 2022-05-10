import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Here the traceback is "ValueError: mmap offset is greater than file size".
Just to be clear:
<code>with open('test', 'wb') as f:
    f.write(bytes(5))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
runs fine.
I actually found a solution of this problem, but still want to know why:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(1)  # do not care about the old content
    f.truncate()
    a = m[:]
</code>
What has zeros to do with it?


A:

From the docs:
<blockquote>
<p>resize(newsize)

