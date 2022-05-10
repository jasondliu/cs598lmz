import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The code above raises: <code>ValueError: cannot resize a mmap backed array</code>. According to this issue it is not possible to resize a memory mapped file.
Is there a way to resize the file?


A:

I don't think this is possible.
The workaround is to close the <code>mmap</code> object and reopen the file.

