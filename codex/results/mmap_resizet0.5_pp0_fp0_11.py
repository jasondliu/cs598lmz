import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This works fine on Ubuntu, but on Windows I get <code>ValueError: mmap length is zero</code>.
I know that the file is empty, but I don't know how to fix it.


A:

I found a python bug report about this, and a workaround:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    f.seek(0)
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>

