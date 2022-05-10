import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
It works under Linux but fails under Windows, where IOError is raised from mmap.mmap:
<code>mmap.error: [Errno 22] Invalid argument
</code>
Is there any way to use mmap in such a way (i.e. with truncating file) under Windows?


A:

I think this is a bug in python at https://bugs.python.org/issue26897
Try this, it works:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    m.resize(0)
    a = m[:]
</code>

