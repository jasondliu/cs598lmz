import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The expected result is <code>a</code> is an empty byte array, but it actually gives me a byte array of <code>\x01</code>.
I also tried to use <code>mmap.resize</code> method, but still not working.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    mmap.resize(m, 0)
    a = m[:]
</code>
Can anyone give me a hint on how to truncate the file without losing the mmap?


A:

You can't. mmap doesn't give you a view of the file, it gives you a view of the file's contents. If you truncate the file, the contents of the file change, and the mmap is no longer valid.
If you want to truncate the file, you have to do it before you mmap it, or after you unmap it.

