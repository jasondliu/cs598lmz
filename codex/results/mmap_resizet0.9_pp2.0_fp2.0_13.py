import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This is an example where I can't get away without explicit closing of <code>mmap</code>, but I don't want to introduce an extra variable.
I know I could use <code>with</code> clause on <code>mmap</code>; this is not the question here. I'm curious whether there's a technical reason for the restriction.
Why is there no way to close a file-like object on leaving a <code>with</code> section?


A:

Python already offers an easy way to create a context manager (and it's likely you should use it instead):
<code>from contextlib import contextmanager


@contextmanager
def mmap_context(file, mode):
    m = mmap.mmap(file.fileno(), 0)
    yield m
    m.close()
</code>
To use <code>mmap_context</code>, simply wrap it around <code>mmap.mmap</code>:
<code>...
with mmap_context(f, "r+b") as m:
    ...
</code>

