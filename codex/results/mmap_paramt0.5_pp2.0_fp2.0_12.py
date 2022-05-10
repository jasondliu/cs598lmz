import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(10)
    print(m.size())
    m.close()
</code>
I would expect the file to be resized to 10 bytes, but it's still 1 byte.
I'm using Python 3.6.5.


A:

You need to use the <code>mmap.resize()</code> function (no parentheses):
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    mmap.resize(m, 10)
    print(m.size())
    m.close()
</code>

