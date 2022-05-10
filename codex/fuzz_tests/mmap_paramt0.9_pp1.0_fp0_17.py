import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1, access = mmap.ACCESS_WRITE)
    m[0] = 0b10000000
</code>
This program crashes because the <code>ACCESS_WRITE</code> flag isn't supported. 
I am currently using this workaround:
<code>with open('test', 'r') as f:
    m = mmap.mmap(f.fileno(), 1, access = mmap.ACCESS_READ)
with open('test', 'r+') as f:
    m = mmap.mmap(f.fileno(), 1, access = mmap.ACCESS_WRITE)
</code>
Is there a less clunky way to do this?


A:

It might be a bit of a hack, but by this do you mean that you just want the handle <code>m</code> to be available for writing?
In this case, I did the next thing that occurred to me:

Create a virtual file that gets deleted automatically on process exit by using <code>tempfile.NamedTemporaryFile.seek(0)</code>. [This is very fast, since it appears in
